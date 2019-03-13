from .prep_filters import FilterPrepareSetH
from app.model.condition import ConditionMaker
#===============================================
def defineFilterSchema():
    filters = FilterPrepareSetH()

    filters.zygositySpecialUnit("zygosity",
        "/data/zygosity", title = "zygosity",
        config = {"x_cond":
            ConditionMaker.condEnum("Chromosome", ["chrX"])})

    with filters.viewGroup("Coordinates"):
        filters.statusUnit("Chromosome", "/_filters/chromosome",
            ["chr1", "chr2", "chr3", "chr4", "chr5",
            "chr6", "chr7", "chr8", "chr9", "chr10",
            "chr11", "chr12", "chr13", "chr14", "chr15",
            "chr16", "chr17", "chr18", "chr19", "chr20",
            "chr21", "chr22", "chr23", "chrX", "chrY", "?"],
        research_only = True, accept_other_values = True)

        filters.statusUnit("Chromosome", "/data/seq_region_name",
            research_only = True)

        filters.intValueUnit("Start_Pos", "/data/start",
            title = "Start Position", research_only = True)
        filters.intValueUnit("End_Pos", "/data/end",
            title = "End Position", research_only = True)
        filters.intValueUnit("Dist_from_Exon", "/_filters/dist_from_exon",
            title = "Distance From Intron/Exon Boundary (Canonical)",
            research_only = False, default_value = 0)
        filters.statusUnit("Region", "/data/region_canonical",
            title = "Region (Canonical)",
            research_only = False, default_value = "Other")

    filters.multiStatusUnit("Genes", "/view/general/genes[]",
        compact_mode = True)

    filters.statusUnit("Most_Severe_Consequence",
        "/data/most_severe_consequence",
        variants = ["transcript_ablation",
        "splice_acceptor_variant",
        "splice_donor_variant",
        "stop_gained",
        "frameshift_variant",
        "stop_lost",
        "start_lost",
        "transcript_amplification",
        "inframe_insertion",
        "inframe_deletion",
        "missense_variant",
        "protein_altering_variant",
        "incomplete_terminal_codon_variant",
        "stop_retained_variant",
        "synonymous_variant",
        "splice_region_variant",
        "coding_sequence_variant",
        "mature_miRNA_variant",
        "5_prime_UTR_variant",
        "3_prime_UTR_variant",
        "non_coding_transcript_exon_variant",
        "intron_variant",
        "NMD_transcript_variant",
        "non_coding_transcript_variant",
        "upstream_gene_variant",
        "downstream_gene_variant",
        "TFBS_ablation",
        "TFBS_amplification",
        "TF_binding_site_variant",
        "regulatory_region_ablation",
        "regulatory_region_amplification",
        "feature_elongation",
        "regulatory_region_variant",
        "feature_truncation",
        "intergenic_variant",
        "undefined"], default_value = "undefined")

    with filters.viewGroup("gnomAD"):
        filters.floatValueUnit("gnomAD_AF",
            "/_filters/gnomad_af_fam",
            diap = (0., 1.), default_value = 0.,
            title = "gnomAD Allele Frequency (family)")
        filters.floatValueUnit("gnomAD_AF_Exomes",
            "/_filters/gnomad_db_exomes_af",
            diap = (0., 1.), default_value = 0.,
            title = "gnomAD Exome Allele Frequency (family)")
        filters.floatValueUnit("gnomAD_AF_Genomes",
            "/_filters/gnomad_db_genomes_af",
            diap = (0., 1.), default_value = 0.,
            title = "gnomAD Genome Allele Frequency (family)")
        filters.floatValueUnit("gnomAD_AF_Proband",
            "/_filters/gnomad_af_pb",
            diap = (0., 1.), default_value = 0.,
            title = "gnomAD Allele Frequency (proband)")
        filters.floatValueUnit("gnomAD_PopMax_AF",
            "/_filters/gnomad_popmax_af",
            diap = (0., 1.), default_value = 0.,
            title = "gnomAD PopMax Allele Frequency")
        filters.statusUnit("gnomAD_PopMax",
            "/_filters/gnomad_popmax", default_value = "None",
            title = "gnomAD PopMax Ancestry")
        filters.intValueUnit("gnomAD_PopMax_AN",
            "/_filters/gnomad_popmax_an",
            default_value = 0,
            title = "gnomAD: Number of alleles in PopMax Ancestry")

    with filters.viewGroup("Databases"):
        filters.presenceUnit("Presence_in_Databases", [
            ("ClinVar", "/view/databases/clinVar"),
            ("LMM", "/view/databases/lmm_significance"),
            ("GeneDx", "/view/databases/gene_dx_significance"),
            ("GnomAD", "/_filters/gnomad_af_fam"),
            ("HGMD", "/view/databases/hgmd_pmids[]"),
            ("OMIM", "/view/databases/omim")])

        filters.multiStatusUnit("ClinVar_Submitters",
            "/view/databases/clinVar_submitters[]",
            title = "ClinVar Submitters")

        # filters.multiStatusUnit("beacons",
        #     "/data/beacon_names",
        #     title = "Observed at")

    with filters.viewGroup("Call"):
        filters.statusUnit("Variant_Class", "/data/variant_class")
        filters.multiStatusUnit("Callers", "/view/bioinformatics/called_by[]",
            title = "Called by", research_only = False)
        filters.multiStatusUnit("Has_Variant", "/_filters/has_variant[]")

    with filters.viewGroup("Call_Quality"):
        filters.intValueUnit("Proband_GQ", "/_filters/proband_gq")
        filters.intValueUnit("Min_GQ", "/_filters/min_gq")
        filters.intValueUnit("QD", "/_filters/qd")
        filters.intValueUnit("FS", "/_filters/fs")
        filters.multiStatusUnit("FT", "/_filters/filters[]", title="FILTER")

    with filters.viewGroup("Predictions"):
        filters.statusUnit("Clinvar_Benign", "/_filters/clinvar_benign",
            default_value = "Not in ClinVar")
        filters.statusUnit("Clinvar_Trusted_Benign",
            "/_filters/clinvar_trusted_benign",
            default_value = "No data",
            title = "Benign by Clinvar Trusted Submitters")
        filters.statusUnit("HGMD_Benign", "/_filters/hgmd_benign",
            default_value = "Not in HGMD")

        filters.multiStatusUnit("HGMD_Tags", "/view/databases/hgmd_tags[]",
            default_value = "None")
        filters.multiStatusUnit("ClinVar_Significance",
            "/data/clinvar_significance[]")
        filters.multiStatusUnit("LMM_Significance",
            "/data/lmm", title = "Clinical Significance by LMM")
        filters.multiStatusUnit("GeneDx_Significance",
            "/data/gene_dx", title = "Clinical Significance by GeneDx")

        filters.multiStatusUnit("Polyphen", "/view/predictions/polyphen[]")
        filters.multiStatusUnit("SIFT", "/view/predictions/sift[]")

        filters.multiStatusUnit("Polyphen_2_HVAR",
            "/view/predictions/polyphen2_hvar[]",
            separators = "[\s\,]", default_value = "undef")
        filters.multiStatusUnit("Polyphen_2_HDIV",
            "/view/predictions/polyphen2_hdiv[]",
            separators = "[\s\,]", default_value = "undef")

    with filters.viewGroup("Debug_Info"):
        filters.intValueUnit("Severity", "/_filters/severity",
            research_only = True, default_value = -1)

    return filters
