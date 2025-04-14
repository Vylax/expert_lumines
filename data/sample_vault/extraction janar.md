```
select

'adental' as Groupe,

factures.fact_centre_libelle AS Centre,

CONCAT(factures.fact_patient_nom, ' ', factures.fact_patient_prenom) AS Patient,

factures.fact_patient_date_naissance AS Date_de_naissance_patient,

CONCAT(factures.fact_praticien_nom, ' ', factures.fact_praticien_prenom) AS Praticien,

factures.fact_numero as NumFacture,

factures.fact_devis_num as NumDevis,

lf.ligfact_ccam_code as CCAM,

sf.suifact_facture_type as Statut_Fact,

lf.ligfact_acte_realise_date as DateActe,

lf.ligfact_montant_honoraire as Montant,

lf.ligfact_numeros_dents as dents

FROM desmos_adental.factures

inner join lignes_factures lf

on lf.ligfact_idtfact = factures.fact_idtfact

inner join suivi_factures sf

on sf.suifact_facture_id = lf.ligfact_idtfact

where factures.fact_patient_date_naissance < '01/01/2009'

and lf.ligfact_acte_realise_date > '2025-01-01 00:00:00.000';
```