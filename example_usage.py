from client import BiochemicalProteinLigandBindingAffinityPredictorClient

def main():
    client = BiochemicalProteinLigandBindingAffinityPredictorClient()
    res = client.predict_molecular_complex_conformation('6LU7_MAIN_PROTEASE', 'CN1CCN(CC1)C(=O)C2=CC=C(C=C2)NC(=O)C3=CC=CC=C3F')
    print('Screening: ' + res['screening_id'] + ' for ' + res['protein_target_id'])
    print('Binding Affinity (Kd): ' + str(res['predicted_kd_binding_affinity_nm']) + ' nM | RMSD: ' + str(res['docking_rmsd_angstroms']) + ' A')
    print('Multimer Confidence: ' + str(res['all_atom_multimer_confidence_ptm']) + ' | Qualified: ' + str(res['de_novo_small_molecule_drug_candidate_qualified']))

if __name__ == '__main__':
    main()
