from django.db import models

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
    tractpopulation = models.FloatField(blank=True, null=True) # TODO: dummy out some values for years other than 2010
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

    class Meta:
        managed = True
        db_table = 'total_loans'
