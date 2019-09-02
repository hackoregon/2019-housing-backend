from django.contrib.gis.db import models

class MedianHouseholdIncomeByRace1990T2017Msa(models.Model):
    race_explicit = models.TextField(blank=True, null=True)
    year = models.FloatField(blank=True, null=True)
    adjusted_median_income = models.FloatField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    aggregation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'median_household_income_by_race_1990t2017_msa'

class Sc2HmdaApprovalByRace2013T2017(models.Model):
    geoid = models.TextField(db_column='GEOID', blank=True, null=True)  # Field name made lowercase.
    datayear = models.FloatField(db_column='DATAYEAR', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(blank=True, null=True)
    total_hh = models.FloatField(blank=True, null=True)
    total_own = models.FloatField(blank=True, null=True)
    share_own = models.FloatField(blank=True, null=True)
    total_hh_white = models.FloatField(blank=True, null=True)
    total_own_white = models.FloatField(blank=True, null=True)
    share_own_white = models.FloatField(blank=True, null=True)
    total_hh_black = models.FloatField(blank=True, null=True)
    total_own_black = models.FloatField(blank=True, null=True)
    share_own_black = models.FloatField(blank=True, null=True)
    total_hh_aian = models.FloatField(blank=True, null=True)
    total_own_aian = models.FloatField(blank=True, null=True)
    share_own_aian = models.FloatField(blank=True, null=True)
    total_hh_api = models.FloatField(blank=True, null=True)
    total_own_api = models.FloatField(blank=True, null=True)
    share_own_api = models.FloatField(blank=True, null=True)
    total_hh_other = models.FloatField(blank=True, null=True)
    total_own_other = models.FloatField(blank=True, null=True)
    share_own_other = models.FloatField(blank=True, null=True)
    total_hh_multi = models.FloatField(blank=True, null=True)
    total_own_multi = models.FloatField(blank=True, null=True)
    share_own_multi = models.FloatField(blank=True, null=True)
    total_hh_hisp = models.FloatField(blank=True, null=True)
    total_own_hisp = models.FloatField(blank=True, null=True)
    share_own_hisp = models.FloatField(blank=True, null=True)
    share_total_own_white = models.FloatField(blank=True, null=True)
    share_total_own_black = models.FloatField(blank=True, null=True)
    share_total_own_aian = models.FloatField(blank=True, null=True)
    share_total_own_api = models.FloatField(blank=True, null=True)
    share_total_own_other = models.FloatField(blank=True, null=True)
    share_total_own_multi = models.FloatField(blank=True, null=True)
    share_total_own_hisp = models.FloatField(blank=True, null=True)
    loans_total = models.FloatField(blank=True, null=True)
    loans_white = models.FloatField(blank=True, null=True)
    loans_black = models.FloatField(blank=True, null=True)
    loans_aian = models.FloatField(blank=True, null=True)
    loans_api = models.FloatField(blank=True, null=True)
    loans_multi = models.FloatField(blank=True, null=True)
    loans_hisp = models.FloatField(blank=True, null=True)
    loans_share_white = models.FloatField(blank=True, null=True)
    loans_share_black = models.FloatField(blank=True, null=True)
    loans_share_aian = models.FloatField(blank=True, null=True)
    loans_share_api = models.FloatField(blank=True, null=True)
    loans_share_multi = models.FloatField(blank=True, null=True)
    loans_share_hisp = models.FloatField(blank=True, null=True)
    lq_white = models.FloatField(blank=True, null=True)
    lq_black = models.FloatField(blank=True, null=True)
    lq_aian = models.FloatField(blank=True, null=True)
    lq_api = models.FloatField(blank=True, null=True)
    lq_multi = models.FloatField(blank=True, null=True)
    lq_hisp = models.FloatField(blank=True, null=True)
    lq_white_brks = models.TextField(db_column='lq_white.brks', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lq_black_brks = models.TextField(db_column='lq_black.brks', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lq_aian_brks = models.TextField(db_column='lq_aian.brks', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lq_api_brks = models.TextField(db_column='lq_api.brks', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lq_multi_brks = models.TextField(db_column='lq_multi.brks', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lq_hisp_brks = models.TextField(db_column='lq_hisp.brks', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    aland = models.FloatField(db_column='ALAND', blank=True, null=True)  # Field name made lowercase.
    awater = models.FloatField(db_column='AWATER', blank=True, null=True)  # Field name made lowercase.
    geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    tract_geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SC2_hmda_approval_by_race_2013t2017'

class MultnomahHomeOwnershipByRace(models.Model):
    yr = models.FloatField(blank=True, null=True)
    race = models.TextField(blank=True, null=True)
    home_ownership_rate = models.FloatField(blank=True, null=True)
    home_ownership_count = models.FloatField(blank=True, null=True)
    household_count = models.FloatField(blank=True, null=True)
    geoname = models.TextField(blank=True, null=True)
    fips = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multnomah_home_ownership_by_race'

class PortlandHomeAppreciationAnnuallySince1990Ish(models.Model):
    prev_sale_year = models.TextField(blank=True, null=True)
    sale_year = models.IntegerField(blank=True, null=True)
    raw_appreciation_mean = models.FloatField(blank=True, null=True)
    raw_appreciation_25th = models.FloatField(blank=True, null=True)
    raw_appreciation_75th = models.FloatField(blank=True, null=True)
    raw_appreciation_med = models.FloatField(blank=True, null=True)
    adj_appreciation_mean = models.FloatField(blank=True, null=True)
    adj_appreciation_25th = models.FloatField(blank=True, null=True)
    adj_appreciation_75th = models.FloatField(blank=True, null=True)
    adj_appreciation_med = models.FloatField(blank=True, null=True)
    count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portland_home_appreciation_annually_since_1990ish'

class HomeInflationKriging(models.Model):
    appreciation_estimates = models.FloatField(blank=True, null=True)
    geometry = models.GeometryField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'home_inflation_kriging'

class ResidentialBuildingPermitData(models.Model):
    index = models.BigIntegerField(primary_key=True)
    x = models.FloatField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.FloatField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    indate = models.TextField(db_column='INDATE', blank=True, null=True)  # Field name made lowercase.
    issuedate = models.TextField(db_column='ISSUEDATE', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    year_field = models.BigIntegerField(db_column='YEAR_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    newclass = models.TextField(db_column='NEWCLASS', blank=True, null=True)  # Field name made lowercase.
    newtype = models.TextField(db_column='NEWTYPE', blank=True, null=True)  # Field name made lowercase.
    nbrhood = models.TextField(db_column='NBRHOOD', blank=True, null=True)  # Field name made lowercase.
    pdxbnd = models.TextField(db_column='PDXBND', blank=True, null=True)  # Field name made lowercase.
    is_adu = models.NullBooleanField(db_column='IS_ADU')  # Field name made lowercase.
    rev = models.TextField(db_column='REV', blank=True, null=True)  # Field name made lowercase.
    foldernumb = models.TextField(db_column='FOLDERNUMB', blank=True, null=True)  # Field name made lowercase.
    prop_addre = models.TextField(db_column='PROP_ADDRE', blank=True, null=True)  # Field name made lowercase.
    workdesc = models.TextField(db_column='WORKDESC', blank=True, null=True)  # Field name made lowercase.
    sub = models.TextField(db_column='SUB', blank=True, null=True)  # Field name made lowercase.
    occ = models.TextField(db_column='OCC', blank=True, null=True)  # Field name made lowercase.
    new_units = models.BigIntegerField(db_column='NEW_UNITS', blank=True, null=True)  # Field name made lowercase.
    folder_des = models.TextField(db_column='FOLDER_DES', blank=True, null=True)  # Field name made lowercase.
    valuation = models.BigIntegerField(db_column='VALUATION', blank=True, null=True)  # Field name made lowercase.
    const = models.TextField(db_column='CONST', blank=True, null=True)  # Field name made lowercase.
    proplot = models.TextField(db_column='PROPLOT', blank=True, null=True)  # Field name made lowercase.
    propgisid1 = models.TextField(db_column='PROPGISID1', blank=True, null=True)  # Field name made lowercase.
    propertyro = models.TextField(db_column='PROPERTYRO', blank=True, null=True)  # Field name made lowercase.
    folderrsn = models.BigIntegerField(db_column='FOLDERRSN', blank=True, null=True)  # Field name made lowercase.
    x_coord = models.FloatField(db_column='X_COORD', blank=True, null=True)  # Field name made lowercase.
    y_coord = models.FloatField(db_column='Y_COORD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'residential_building_permit_data'

class NcdbSampleChanges(models.Model):
    fips_code = models.ForeignKey('FIPSRecords', null=True, on_delete=models.SET_NULL)
    cbsa = models.FloatField(blank=True, null=True)
    metroname = models.TextField(blank=True, null=True)
    tractcontrol = models.BigIntegerField(blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    chrent = models.FloatField(blank=True, null=True)
    chinc = models.FloatField(blank=True, null=True)
    chhomeval = models.FloatField(blank=True, null=True)
    chbachshare = models.FloatField(blank=True, null=True)
    chwhiteshare = models.FloatField(blank=True, null=True)
    chblackshare = models.FloatField(blank=True, null=True)
    chhispshare = models.FloatField(blank=True, null=True)
    chasothshare = models.FloatField(blank=True, null=True)
    chownshare = models.FloatField(blank=True, null=True)
    chpovrate = models.FloatField(blank=True, null=True)
    chrentcbshare = models.FloatField(blank=True, null=True)
    metchinc = models.FloatField(blank=True, null=True)
    metchbachshare = models.FloatField(blank=True, null=True)
    metchrent = models.FloatField(blank=True, null=True)
    metchhomeval = models.FloatField(blank=True, null=True)
    metchpovrate = models.FloatField(blank=True, null=True)
    metchownshare = models.FloatField(blank=True, null=True)
    metchrentcbshare = models.FloatField(blank=True, null=True)
    metchwhiteshare = models.FloatField(blank=True, null=True)
    metchblackshare = models.FloatField(blank=True, null=True)
    metchhispshare = models.FloatField(blank=True, null=True)
    metchasothshare = models.FloatField(blank=True, null=True)

class NcdbSampleYearly(models.Model):
    fips_code = models.ForeignKey('FIPSRecords', null=True, on_delete=models.SET_NULL)
    cbsa = models.FloatField(blank=True, null=True)
    metroname = models.TextField(blank=True, null=True)
    tractcontrol = models.BigIntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    tractpopulation = models.FloatField(blank=True, null=True)
    medinc = models.FloatField(blank=True, null=True)
    medhomeval = models.FloatField(blank=True, null=True)
    medrentval = models.FloatField(blank=True, null=True)
    ownshare = models.FloatField(blank=True, null=True)
    whiteshare = models.FloatField(blank=True, null=True)
    blackshare = models.FloatField(blank=True, null=True)
    hispshare = models.FloatField(blank=True, null=True)
    asothshare = models.FloatField(blank=True, null=True)
    rentcbshare = models.FloatField(blank=True, null=True)
    povrate = models.FloatField(blank=True, null=True)
    bachshare = models.FloatField(blank=True, null=True)
    metmedinc = models.FloatField(blank=True, null=True)
    metmedhomeval = models.FloatField(blank=True, null=True)
    metmedrentval = models.FloatField(blank=True, null=True)
    metownshare = models.FloatField(blank=True, null=True)
    metwhiteshare = models.FloatField(blank=True, null=True)
    metblackshare = models.FloatField(blank=True, null=True)
    methispshare = models.FloatField(blank=True, null=True)
    metasothshare = models.FloatField(blank=True, null=True)
    metrentcbshare = models.FloatField(blank=True, null=True)
    metpovrate = models.FloatField(blank=True, null=True)
    metbachshare = models.FloatField(blank=True, null=True)
    tract_geom = models.GeometryField(blank=True, null=True)

class NcdbMetroYearlyData(models.Model):
    year = models.IntegerField(blank=True, null=True)
    metroname = models.TextField(blank=True, null=True)
    metmedinc = models.FloatField(blank=True, null=True)
    metmedhomeval = models.FloatField(blank=True, null=True)
    metmedrentval = models.FloatField(blank=True, null=True)
    metownshare = models.FloatField(blank=True, null=True)
    metwhiteshare = models.FloatField(blank=True, null=True)
    metblackshare = models.FloatField(blank=True, null=True)
    methispshare = models.FloatField(blank=True, null=True)
    metasothshare = models.FloatField(blank=True, null=True)
    metrentcbshare = models.FloatField(blank=True, null=True)
    metpovrate = models.FloatField(blank=True, null=True)
    metbachshare = models.FloatField(blank=True, null=True)

class FIPSRecords(models.Model):
    geo_fips = models.BigIntegerField(primary_key=True)
    geo_state = models.FloatField(blank=True, null=True)
    geo_county = models.FloatField(blank=True, null=True)
    geo_tract = models.FloatField(blank=True, null=True)

class HmdaOrwa(models.Model):
    index = models.BigIntegerField(primary_key=True)
    year = models.TextField(blank=True, null=True)
    actiontakentype = models.TextField(db_column='ActionTakenType', blank=True, null=True)  # Field name made lowercase.
    agencyname = models.TextField(db_column='AgencyName', blank=True, null=True)  # Field name made lowercase.
    applicant1_sex_name = models.TextField(blank=True, null=True)
    applicant1race = models.TextField(db_column='Applicant1Race', blank=True, null=True)  # Field name made lowercase.
    applicant2_sex_name = models.TextField(blank=True, null=True)
    applicant2race = models.TextField(db_column='Applicant2Race', blank=True, null=True)  # Field name made lowercase.
    applicantincome = models.IntegerField(db_column='ApplicantIncome', blank=True, null=True)  # Field name made lowercase.
    censustract = models.TextField(db_column='CensusTract', blank=True, null=True)  # Field name made lowercase.
    countycode = models.TextField(db_column='CountyCode', blank=True, null=True)  # Field name made lowercase.
    denialreason1 = models.TextField(db_column='DenialReason1', blank=True, null=True)  # Field name made lowercase.
    denialreason2 = models.TextField(db_column='DenialReason2', blank=True, null=True)  # Field name made lowercase.
    denialreason3 = models.TextField(db_column='DenialReason3', blank=True, null=True)  # Field name made lowercase.
    editstatus = models.TextField(db_column='EditStatus', blank=True, null=True)  # Field name made lowercase.
    hoepa_loan = models.TextField(db_column='HOEPA_loan', blank=True, null=True)  # Field name made lowercase.
    hud_median_family_income = models.IntegerField(blank=True, null=True)
    lienstatus = models.TextField(db_column='LienStatus', blank=True, null=True)  # Field name made lowercase.
    loanamount = models.IntegerField(db_column='LoanAmount', blank=True, null=True)  # Field name made lowercase.
    loanpurpose = models.TextField(db_column='LoanPurpose', blank=True, null=True)  # Field name made lowercase.
    loantype = models.TextField(db_column='LoanType', blank=True, null=True)  # Field name made lowercase.
    minority_population = models.FloatField(blank=True, null=True)
    msaofproperty = models.TextField(db_column='MSAofProperty', blank=True, null=True)  # Field name made lowercase.
    number_of_1_to_4_family_units = models.IntegerField(blank=True, null=True)
    number_of_owner_occupied_units = models.IntegerField(blank=True, null=True)
    occupancy = models.TextField(db_column='Occupancy', blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(blank=True, null=True)
    preapprovals = models.TextField(db_column='Preapprovals', blank=True, null=True)  # Field name made lowercase.
    propertytype = models.TextField(db_column='PropertyType', blank=True, null=True)  # Field name made lowercase.
    purchasertype = models.TextField(db_column='PurchaserType', blank=True, null=True)  # Field name made lowercase.
    ratespread = models.FloatField(db_column='RateSpread', blank=True, null=True)  # Field name made lowercase.
    respondent_id = models.TextField(db_column='Respondent_ID', blank=True, null=True)  # Field name made lowercase.
    sequencenumber = models.IntegerField(db_column='SequenceNumber', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(blank=True, null=True)
    tract_to_msamd_income = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hmda_orwa'

class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'spatial_ref_sys'

class TotalLoans(models.Model):
    index = models.BigIntegerField(primary_key=True)
    tct_fips = models.BigIntegerField(blank=True, null=True)
    total_loans = models.BigIntegerField(blank=True, null=True)
    total_poc_loans = models.FloatField(blank=True, null=True)
    share_loans_to_poc = models.FloatField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    pop_total = models.BigIntegerField(blank=True, null=True)
    poc_total = models.BigIntegerField(blank=True, null=True)
    share_poc = models.FloatField(blank=True, null=True)
    total_homeowners = models.BigIntegerField(blank=True, null=True)
    poc_owners = models.BigIntegerField(blank=True, null=True)
    share_poc_owners = models.FloatField(blank=True, null=True)
    loan_lq = models.FloatField(blank=True, null=True)
    brks_lq = models.TextField(db_column='brks.lq', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tract_geom = models.GeometryField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'total_loans'

class MedianHouseholdIncomeByRace2017(models.Model):
    geoid = models.TextField(db_column='GEOID', blank=True, null=True)  # Field name made lowercase.
    sumlevel = models.TextField(blank=True, null=True)
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    hh_income_total = models.FloatField(blank=True, null=True)
    hh_income_white = models.FloatField(blank=True, null=True)
    hh_income_black = models.FloatField(blank=True, null=True)
    hh_income_aian = models.FloatField(blank=True, null=True)
    hh_income_asian = models.FloatField(blank=True, null=True)
    hh_income_nhpi = models.FloatField(blank=True, null=True)
    hh_income_other = models.FloatField(blank=True, null=True)
    hh_income_multi = models.FloatField(blank=True, null=True)
    hh_income_whitenh = models.FloatField(blank=True, null=True)
    hh_income_hisp = models.FloatField(blank=True, null=True)
    tract_geom = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'median_household_income_by_race_2017'

class RaceByTenure1990T2017(models.Model):
    datayear = models.FloatField(db_column='DATAYEAR', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(blank=True, null=True)
    tract_fips = models.TextField(blank=True, null=True)
    total_hh = models.FloatField(blank=True, null=True)
    total_own = models.FloatField(blank=True, null=True)
    share_own = models.FloatField(blank=True, null=True)
    total_hh_white = models.FloatField(blank=True, null=True)
    total_own_white = models.FloatField(blank=True, null=True)
    share_own_white = models.FloatField(blank=True, null=True)
    total_hh_black = models.FloatField(blank=True, null=True)
    total_own_black = models.FloatField(blank=True, null=True)
    share_own_black = models.FloatField(blank=True, null=True)
    total_hh_aian = models.FloatField(blank=True, null=True)
    total_own_aian = models.FloatField(blank=True, null=True)
    share_own_aian = models.FloatField(blank=True, null=True)
    total_hh_api = models.FloatField(blank=True, null=True)
    total_own_api = models.FloatField(blank=True, null=True)
    share_own_api = models.FloatField(blank=True, null=True)
    total_hh_other = models.FloatField(blank=True, null=True)
    total_own_other = models.FloatField(blank=True, null=True)
    share_own_other = models.FloatField(blank=True, null=True)
    total_hh_multi = models.FloatField(blank=True, null=True)
    total_own_multi = models.FloatField(blank=True, null=True)
    share_own_multi = models.FloatField(blank=True, null=True)
    total_hh_hisp = models.FloatField(blank=True, null=True)
    total_own_hisp = models.FloatField(blank=True, null=True)
    share_own_hisp = models.FloatField(blank=True, null=True)
    share_total_own_white = models.FloatField(blank=True, null=True)
    share_total_own_black = models.FloatField(blank=True, null=True)
    share_total_own_aian = models.FloatField(blank=True, null=True)
    share_total_own_api = models.FloatField(blank=True, null=True)
    share_total_own_other = models.FloatField(blank=True, null=True)
    share_total_own_multi = models.FloatField(blank=True, null=True)
    share_total_own_hisp = models.FloatField(blank=True, null=True)
    tract_geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'race_by_tenure_1990t2017'

class Tl201041Tabblock10(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    statefp10 = models.CharField(max_length=2, blank=True, null=True)
    countyfp10 = models.CharField(max_length=3, blank=True, null=True)
    tractce10 = models.CharField(max_length=6, blank=True, null=True)
    blockce10 = models.CharField(max_length=4, blank=True, null=True)
    geoid10 = models.CharField(max_length=15, blank=True, null=True)
    name10 = models.CharField(max_length=10, blank=True, null=True)
    mtfcc10 = models.CharField(max_length=5, blank=True, null=True)
    ur10 = models.CharField(max_length=1, blank=True, null=True)
    uace10 = models.CharField(max_length=5, blank=True, null=True)
    uatyp10 = models.CharField(max_length=1, blank=True, null=True)
    funcstat10 = models.CharField(max_length=1, blank=True, null=True)
    aland10 = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    awater10 = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    intptlat10 = models.CharField(max_length=11, blank=True, null=True)
    intptlon10 = models.CharField(max_length=12, blank=True, null=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tl_2010_41_tabblock10'
