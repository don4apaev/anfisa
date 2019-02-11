import app.prepare.val_conv as val_conv
from .flt_supp import SuportFilterField

#===============================================
class FilterPrepareSetH:
    def __init__(self, support_field_seq):
        self.mUnits = []
        self.mVGroups  = dict()
        self.mCurVGroup = None
        self.mSupportFields = [SuportFilterField.create(info)
            for info in support_field_seq]

    def viewGroup(self, view_group_title):
        assert view_group_title not in self.mVGroups
        ret = ViewGroupH(self, view_group_title, len(self.mVGroups))
        self.mVGroups[view_group_title] = ret
        return ret

    def _startViewGroup(self, view_group_h):
        assert self.mCurVGroup is None
        self.mCurVGroup = view_group_h

    def _endViewGroup(self, view_group_h):
        assert self.mCurVGroup is view_group_h
        self.mCurVGroup = None

    def _addUnit(self, unit):
        for conv in self.mUnits:
            assert conv.getName() != unit.getName()
        self.mUnits.append(unit)

    def intValueUnit(self, name, path, title = None,
            default_value = None, diap = None, research_only = False):
        self._addUnit(val_conv.IntConvertor(name, path, title,
            len(self.mUnits), self.mCurVGroup,
            research_only, default_value, diap))

    def floatValueUnit(self, name, path, title = None,
            default_value = None, diap = None, research_only = False):
        self._addUnit(val_conv.FloatConvertor(name, path, title,
            len(self.mUnits), self.mCurVGroup,
            research_only, default_value, diap))

    def statusUnit(self, name, path, title = None,
            variants = None, default_value = "False",
            accept_other_values = False, research_only = False):
        self._addUnit(val_conv.EnumConvertor(name, path, title,
            len(self.mUnits), self.mCurVGroup,
            research_only, True, variants, default_value,
            accept_other_values = accept_other_values))

    def presenceUnit(self, name, var_info_seq, title = None,
            research_only = False):
        self._addUnit(val_conv.PresenceConvertor(name, title,
            len(self.mUnits), self.mCurVGroup,
            research_only, var_info_seq))

    def multiStatusUnit(self, name, path, title = None,
            variants = None, default_value = "False",
            separators = None, compact_mode = False,
            accept_other_values = False, research_only = False):
        self._addUnit(val_conv.EnumConvertor(name, path, title,
            len(self.mUnits), self.mCurVGroup,
            research_only, False, variants, default_value,
            separators = separators, compact_mode = compact_mode,
            accept_other_values = accept_other_values))

    def process(self, rec_no, rec_data):
        result = dict()
        for supp_f in self.mSupportFields:
            supp_f.process(rec_no, rec_data, result)
        for unit in self.mUnits:
            unit.process(rec_no, rec_data, result)
        return result

    def reportProblems(self, output):
        for unit in self.mUnits:
            if unit.getErrorCount() > 0:
                print >> output, "Field %s: %d bad conversions" % (
                    unit.getName(), unit.getErrorCount())
        return True

    def dump(self):
        return [unit.dump() for unit in self.mUnits]

#===============================================
class ViewGroupH:
    def __init__(self, filter_set, title, no):
        self.mFilterSet = filter_set
        self.mTitle = title
        self.mNo = no
        self.mUnits = []

    def __enter__(self):
        self.mFilterSet._startViewGroup(self)
        return self

    def __exit__(self, type, value, traceback):
        self.mFilterSet._endViewGroup(self)

    def addUnit(self, unit):
        self.mUnits.append(unit)

    def getTitle(self):
        return self.mTitle

    def getUnits(self):
        return self.mUnits
