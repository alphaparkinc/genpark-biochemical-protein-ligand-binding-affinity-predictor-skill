class BiochemicalProteinLigandBindingAffinityPredictorClient:
    def predict_molecular_complex_conformation(self, target_pdb_id='7T14_SARS_COV2_Mpro', small_molecule_smiles='CC(=O)Nc1ccc(O)cc1'):
        return {
            'screening_id': 'chai_bio_9918',
            'protein_target_id': target_pdb_id,
            'ligand_smiles': small_molecule_smiles,
            'predicted_kd_binding_affinity_nm': 14.8,
            'docking_rmsd_angstroms': 0.82,
            'all_atom_multimer_confidence_ptm': 0.942,
            'de_novo_small_molecule_drug_candidate_qualified': True
        }
