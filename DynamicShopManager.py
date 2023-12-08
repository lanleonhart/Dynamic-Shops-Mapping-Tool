import csv
import os

# Below is the data set up in nested categories.The top level determines the DEF type to be output into the CSV file on creation.The next level down# Values below in the pair ie[1, 1] = [Quantity, Frequency] Frequency 1 - 10 with 10 being always# This script is designed

categories = {
     "HeatSink": {
                "Engines-T1": {                   
                    "emod_engineslots_xl_periphery": [1, 3],
                    "emod_engineslots_std": [1, 7],
                    "emod_engineslots_xl_center": [1, 4]
                },
                "Engines-T2": {
                    "emod_engineslots_tunedlight": [1, 1],
                    "emod_engineslots_light": [1, 2]
                },
                "HeatSinks-T1": {
                    "Gear_HeatSink_Generic_Standard": [1, 9]
                },
                "HeatSinks-T2": {
                    "Gear_HeatSink_Generic_Double": [1, 1]
                },

                "EngineCore": {
                    "emod_engine_010": [1, 4],
                    "emod_engine_015": [1, 4],
                    "emod_engine_020": [1, 4],
                    "emod_engine_025": [1, 4],
                    "emod_engine_030": [1, 4],
                    "emod_engine_035": [1, 4],
                    "emod_engine_040": [1, 4],
                    "emod_engine_045": [1, 4],
                    "emod_engine_050": [1, 4],
                    "emod_engine_055": [1, 4],
                    "emod_engine_060": [1, 4],
                    "emod_engine_065": [1, 4],
                    "emod_engine_070": [1, 4],
                    "emod_engine_075": [1, 4],
                    "emod_engine_080": [1, 4],
                    "emod_engine_085": [1, 4],
                    "emod_engine_090": [1, 4],
                    "emod_engine_095": [1, 4],
                    "emod_engine_100": [1, 4],
                    "emod_engine_105": [1, 4],
                    "emod_engine_110": [1, 4],
                    "emod_engine_115": [1, 4],
                    "emod_engine_120": [1, 4],
                    "emod_engine_125": [1, 4],
                    "emod_engine_130": [1, 4],
                    "emod_engine_135": [1, 4],
                    "emod_engine_140": [1, 4],
                    "emod_engine_145": [1, 4],
                    "emod_engine_150": [1, 4],
                    "emod_engine_155": [1, 4],
                    "emod_engine_160": [1, 4],
                    "emod_engine_165": [1, 4],
                    "emod_engine_170": [1, 4],
                    "emod_engine_175": [1, 4],
                    "emod_engine_180": [1, 6],
                    "emod_engine_185": [1, 6],
                    "emod_engine_190": [1, 6],
                    "emod_engine_195": [1, 6],
                    "emod_engine_200": [1, 6],
                    "emod_engine_205": [1, 6],
                    "emod_engine_210": [1, 7],
                    "emod_engine_215": [1, 7],
                    "emod_engine_220": [1, 7],
                    "emod_engine_225": [1, 7],
                    "emod_engine_230": [1, 7],
                    "emod_engine_235": [1, 7],
                    "emod_engine_240": [1, 7],
                    "emod_engine_245": [1, 7],
                    "emod_engine_250": [1, 7],
                    "emod_engine_255": [1, 7],
                    "emod_engine_260": [1, 7],
                    "emod_engine_265": [1, 7],
                    "emod_engine_270": [1, 7],
                    "emod_engine_275": [1, 7],
                    "emod_engine_280": [1, 7],
                    "emod_engine_285": [1, 7],
                    "emod_engine_290": [1, 6],
                    "emod_engine_295": [1, 6],
                    "emod_engine_300": [1, 6],
                    "emod_engine_305": [1, 6],
                    "emod_engine_310": [1, 6],
                    "emod_engine_315": [1, 6],
                    "emod_engine_320": [1, 6],
                    "emod_engine_325": [1, 4],
                    "emod_engine_330": [1, 4],
                    "emod_engine_335": [1, 4],
                    "emod_engine_340": [1, 4],
                    "emod_engine_345": [1, 4],
                    "emod_engine_350": [1, 4],
                    "emod_engine_355": [1, 4],
                    "emod_engine_360": [1, 4],
                    "emod_engine_365": [1, 4],
                    "emod_engine_370": [1, 4],
                    "emod_engine_375": [1, 4],
                    "emod_engine_380": [1, 4],
                    "emod_engine_385": [1, 4],
                    "emod_engine_390": [1, 4],
                    "emod_engine_395": [1, 4],
                    "emod_engine_400": [1, 4]
                },
                "HSKits": {
                    "emod_kit_dhs": [1, 2],
                    "emod_kit_shs": [1, 8]
                }
                },
        "JumpJet": {
        "JumpJets": {
        "Gear_JumpJet_Generic_Assault": [1, 1],
        "Gear_JumpJet_Generic_Heavy": [1, 1],
        "Gear_JumpJet_Generic_Standard": [1, 1]
        }
},        
   "Upgrade": {
    "Actuators": {
        "Gear_Arm_Acc_EnhancedMount": [1, 5],
        "Gear_Arm_Acc_Mount": [1, 5],
        "Gear_Arm_Armor_ArmoredActuator": [1, 6],
        "Gear_Arm_Armor_ReinforcedActuator": [1, 6],
        "Gear_Arm_Armor_Stripped": [1, 7],
        "Gear_Arm_Armor_Stripped-Lower": [1, 7],
        "Gear_Arm_Heat_AdvCoolingCircuit": [1, 3],
        "Gear_Arm_Heat_CoolingCircuit": [1, 1],
        "Gear_Arm_LOS_WideRangeActuators": [1, 2],
        "Gear_Leg_JJ_EnhancedVectorMotors": [1, 3],
        "Gear_Leg_JJ_VectorMotors": [1, 4],
        "Gear_Leg_STAB_Clamp": [1, 4],
        "Gear_Leg_STAB_ReinforcedJoints": [1, 5],
        "Gear_Leg_STAB_ReinforcedJoints_L": [1, 5],
        "Gear_Leg_WT_ScarecrowLegs": [1, 5]
    },
    "Armor-T1": {
        "emod_armorslots_ferrosfibrous": [1, 7]
    },
    "Armor-T2": {
        "emod_armorslots_ferrosfibrousheavy": [1, 5],
        "emod_armorslots_ferrosfibrouslight": [1, 4]
    },
    "Structure-T1": {
        "emod_structureslots_endosteel": [1, 5],
        "emod_structureslots_reinforced": [1, 4]
    },
    "Structure-T2": {
        "emod_structureslots_endocomposite": [1, 4],
        "emod_structureslots_composite": [1, 4]
    },
    "Cockpit": {
        "Gear_Cockpit_CommandConsole": [1, 4],
        "Gear_Cockpit_Small": [1, 6]
    },
    "Life_Support": {
        "Gear_Cockpit_LifeSupportA_Piloting": [1, 6],
        "Gear_Cockpit_LifeSupportA_Tactics": [1, 6],
        "Gear_Cockpit_LifeSupportB_Gunnery": [1, 6],
        "Gear_Cockpit_LifeSupportB_Guts": [1, 6],
        "Gear_Cockpit_LifeSupportB_Piloting": [1, 6],
        "Gear_Cockpit_LifeSupportB_Tactics": [1, 6],
        "Gear_Cockpit_LifeSupportA_Gunnery": [1, 6],
        "Gear_Cockpit_LifeSupportA_Guts": [1, 6]
    },
    "ECM": {
        "Gear_ECM_Angel": [1, 2],
        "Gear_ECM_BAP": [1, 3],
        "Gear_ECM_EWS": [1, 2],
        "Gear_ECM_Guardian": [1, 2]
    },
    "Gyro": {
        "Gear_Gyro_Compact": [1, 5],
        "Gear_Gyro_Hardened": [1, 6],
        "Gear_Gyro_Light": [1, 6],
        "Gear_Gyro_Stabilized": [1, 4],
        "Gear_Gyro_UltraLight": [1, 3]
    },
    "Upgrades": {
        "Gear_ForcedCooler": [1, 2],
        "Gear_MASC": [1, 4],
        "Gear_Supercharger": [1, 5],
        "Gear_TSM": [1, 5]
    }
    },
        "Weapon": {
            "Lasers": {
                "Weapon_Laser_LargeLaser_0-STOCK": [1, 8],
                "Weapon_Laser_LargeLaser_1-Diverse_Optics": [1, 7],
                "Weapon_Laser_LargeLaser_1-ExoStar": [1, 7],
                "Weapon_Laser_LargeLaser_1-Intek": [1, 7],
                "Weapon_Laser_LargeLaser_2-Diverse_Optics": [1, 6],
                "Weapon_Laser_LargeLaser_2-ExoStar": [1, 6],
                "Weapon_Laser_LargeLaser_2-Intek": [1, 6],
                "Weapon_Laser_LargeLaser_2-Magna": [1, 6],
                "Weapon_Laser_MediumLaser_0-STOCK": [1, 8],
                "Weapon_Laser_MediumLaser_1-ExoStar": [1, 7],
                "Weapon_Laser_MediumLaser_1-Intek": [1, 7],
                "Weapon_Laser_MediumLaser_1-Magna": [1, 7],
                "Weapon_Laser_MediumLaser_2-Diverse_Optics": [1, 6],
                "Weapon_Laser_MediumLaser_2-ExoStar": [1, 6],
                "Weapon_Laser_MediumLaser_2-Intek": [1, 6],
                "Weapon_Laser_MediumLaser_2-Magna": [1, 6],
                "Weapon_Laser_MediumLaser_3-Diverse_Optics": [1, 5],
                "Weapon_Laser_SmallLaser_0-STOCK": [1, 8],
                "Weapon_Laser_SmallLaser_1-Diverse_Optics": [1, 7],
                "Weapon_Laser_SmallLaser_1-ExoStar": [1, 7],
                "Weapon_Laser_SmallLaser_1-Magna": [1, 7],
                "Weapon_Laser_SmallLaser_2-Diverse_Optics": [1, 6],
                "Weapon_Laser_SmallLaser_2-ExoStar": [1, 6],
                "Weapon_Laser_SmallLaser_2-Intek": [1, 6],
                "Weapon_Laser_SmallLaser_2-Magna": [1, 6],
                "Weapon_Laser_SmallLaser_3-Intek": [1, 6],
            },
            "ERLasers": {
                "Weapon_Laser_SmallLaserER_0-STOCK": [1, 6],
                "Weapon_Laser_SmallLaserER_1-Diverse_Optics": [1, 5],
                "Weapon_Laser_SmallLaserER_2-BlazeFire": [1, 4],
                "Weapon_Laser_MediumLaserER_0-STOCK": [1, 6],
                "Weapon_Laser_MediumLaserER_1-MagnaVI": [1, 5],
                "Weapon_Laser_MediumLaserER_2-BrightBloom": [1, 4],
                "Weapon_Laser_LargeLaserER_0-STOCK": [1, 6],
                "Weapon_Laser_LargeLaserER_1-Blankenburg25": [1, 5],
                "Weapon_Laser_LargeLaserER_2-BlazeFire": [1, 4],
            },
            "PulseLasers": {
                "Weapon_Laser_LargeLaserPulse_0-STOCK": [1, 5],
                "Weapon_Laser_LargeLaserPulse_1-Thunderbolt12": [1, 5],
                "Weapon_Laser_LargeLaserPulse_2-Exostar": [1, 4],
                "Weapon_Laser_MediumLaserPulse_0-STOCK": [1, 5],
                "Weapon_Laser_MediumLaserPulse_1-RakerIV": [1, 5],
                "Weapon_Laser_MediumLaserPulse_2-Magna400P": [1, 4],
                "Weapon_Laser_SmallLaserPulse_0-STOCK": [1, 5],
                "Weapon_Laser_SmallLaserPulse_1-Maxell": [1, 5],
                "Weapon_Laser_SmallLaserPulse_2-Magna200P": [1, 4],
            },
            "PPC": {
                "Weapon_PPC_PPC_0-STOCK": [1, 7],
                "Weapon_PPC_PPC_1-Ceres_Arms": [1, 6],
                "Weapon_PPC_PPC_1-Donal": [1, 6],
                "Weapon_PPC_PPC_1-Tiegart": [1, 6],
                "Weapon_PPC_PPC_2-Ceres_Arms": [1, 5],
                "Weapon_PPC_PPC_2-Donal": [1, 5],
                "Weapon_PPC_PPC_2-Tiegart": [1, 5],
                "Weapon_PPC_PPCER_0-STOCK": [1, 6],
                "Weapon_PPC_PPCER_1-MagnaFirestar": [1, 5],
                "Weapon_PPC_PPCER_2-TiegartMagnum": [1, 5],
                "Weapon_PPC_PPCSnub_0-STOCK": [1, 6],
                "Weapon_PPC_PPCSnub_1-Ceres_Arms": [1, 6],
                "Weapon_PPC_PPCSnub_1-Donal": [1, 6],
                "Weapon_PPC_PPCSnub_1-Magna": [1, 6],
                "Weapon_PPC_PPCSnub_2-Ceres_Arms": [1, 5],
                "Weapon_PPC_PPCSnub_2-Donal": [1, 5],
                "Weapon_PPC_PPCSnub_2-Magna": [1, 5],
            },
            "Autocannon": {
                "Weapon_Autocannon_AC2_0-STOCK": [1, 8],
                "Weapon_Autocannon_AC2_1-Defiance": [1, 7],
                "Weapon_Autocannon_AC2_1-Federated": [1, 7],
                "Weapon_Autocannon_AC2_1-Kali_Yama": [1, 7],
                "Weapon_Autocannon_AC2_1-Mydron": [1, 7],
                "Weapon_Autocannon_AC2_2-Defiance": [1, 6],
                "Weapon_Autocannon_AC2_2-Federated": [1, 6],
                "Weapon_Autocannon_AC2_2-Imperator": [1, 6],
                "Weapon_Autocannon_AC2_2-Kali_Yama": [1, 6],
                "Weapon_Autocannon_AC2_2-Mydron": [1, 6],
                "Weapon_Autocannon_AC2_3-Imperator": [1, 5],
                "Weapon_Autocannon_AC5_0-STOCK": [1, 8],
                "Weapon_Autocannon_AC5_1-Defiance": [1, 7],
                "Weapon_Autocannon_AC5_1-Federated": [1, 7],
                "Weapon_Autocannon_AC5_1-Imperator": [1, 7],
                "Weapon_Autocannon_AC5_1-Kali_Yama": [1, 7],
                "Weapon_Autocannon_AC5_2-Defiance": [1, 6],
                "Weapon_Autocannon_AC5_2-Federated": [1, 6],
                "Weapon_Autocannon_AC5_2-Imperator": [1, 6],
                "Weapon_Autocannon_AC5_2-Kali_Yama": [1, 6],
                "Weapon_Autocannon_AC5_2-Mydron": [1, 6],
                "Weapon_Autocannon_AC5_3-Mydron": [1, 5],
            },
            "Autocannon_Large": {
                "Weapon_Autocannon_AC10_0-STOCK": [1, 7],
                "Weapon_Autocannon_AC10_1-Defiance": [1, 6],
                "Weapon_Autocannon_AC10_1-Imperator": [1, 6],
                "Weapon_Autocannon_AC10_1-Kali_Yama": [1, 6],
                "Weapon_Autocannon_AC10_1-Mydron": [1, 6],
                "Weapon_Autocannon_AC10_2-Defiance": [1, 6],
                "Weapon_Autocannon_AC10_2-Federated": [1, 6],
                "Weapon_Autocannon_AC10_2-Imperator": [1, 6],
                "Weapon_Autocannon_AC10_2-Kali_Yama": [1, 6],
                "Weapon_Autocannon_AC10_2-Mydron": [1, 6],
                "Weapon_Autocannon_AC10_3-Federated": [1, 5],
                "Weapon_Autocannon_AC20_0-STOCK": [1, 7],
                "Weapon_Autocannon_AC20_1-Defiance": [1, 6],
                "Weapon_Autocannon_AC20_1-Federated": [1, 6],
                "Weapon_Autocannon_AC20_1-Imperator": [1, 6],
                "Weapon_Autocannon_AC20_1-Mydron": [1, 6],
                "Weapon_Autocannon_AC20_2-Defiance": [1, 5],
                "Weapon_Autocannon_AC20_2-Federated": [1, 5],
                "Weapon_Autocannon_AC20_2-Imperator": [1, 5],
                "Weapon_Autocannon_AC20_2-Kali_Yama": [1, 5],
                "Weapon_Autocannon_AC20_2-Mydron": [1, 5],
                "Weapon_Autocannon_AC20_3-Kali_Yama": [1, 4],
                "Weapon_Autocannon_AC20_SPECIAL-Victoria": [1, 1],
            },
            "UAC": {
                "Weapon_Autocannon_UAC2_0-STOCK": [1, 5],
                "Weapon_Autocannon_UAC2_1-Imperator": [1, 4],
                "Weapon_Autocannon_UAC2_2-Imperator": [1, 3],
                "Weapon_Autocannon_UAC5_0-STOCK": [1, 5],
                "Weapon_Autocannon_UAC5_1-Mydron": [1, 4],
                "Weapon_Autocannon_UAC5_2-Mydron": [1, 3],
                "Weapon_Autocannon_UAC10_0-STOCK": [1, 5],
                "Weapon_Autocannon_UAC10_1-Federated": [1, 4],
                "Weapon_Autocannon_UAC10_2-Federated": [1, 3],
                "Weapon_Autocannon_UAC20_0-STOCK": [1, 5],
                "Weapon_Autocannon_UAC20_1-Kali_Yama": [1, 4],
                "Weapon_Autocannon_UAC20_2-Kali_Yama": [1, 3],
            },
            "LBX": {
                "Weapon_Autocannon_LB2X_0-STOCK": [1, 6],
                "Weapon_Autocannon_LB2X_1-Defiance": [1, 5],
                "Weapon_Autocannon_LB2X_2-Defiance": [1, 4],
                "Weapon_Autocannon_LB5X_0-STOCK": [1, 6],
                "Weapon_Autocannon_LB5X_1-GM": [1, 5],
                "Weapon_Autocannon_LB5X_2-GM": [1, 4],
                "Weapon_Autocannon_LB10X_0-STOCK": [1, 6],
                "Weapon_Autocannon_LB10X_1-Western": [1, 5],
                "Weapon_Autocannon_LB10X_2-Western": [1, 4],
                "Weapon_Autocannon_LB20X_0-STOCK": [1, 6],
                "Weapon_Autocannon_LB20X_1-Shengli_Arms": [1, 5],
                "Weapon_Autocannon_LB20X_2-Shengli_Arms": [1, 4],
            },
            "HVAC": {
                "Weapon_Autocannon_HVAC2_0-STOCK": [1, 3],
                "Weapon_Autocannon_HVAC5_0-STOCK": [1, 3],
                "Weapon_Autocannon_HVAC10_0-STOCK": [1, 3],
                "Weapon_Autocannon_HVAC20_0-STOCK": [1, 3],
            },
            "MachineGun": {
                "Weapon_MachineGun_MachineGun_0-STOCK": [1, 9],
                "Weapon_MachineGun_MachineGun_1-Brigadier": [1, 8],
                "Weapon_MachineGun_MachineGun_1-VMI": [1, 8],
                "Weapon_MachineGun_MachineGun_2-Brigadier": [1, 7],
                "Weapon_MachineGun_MachineGun_2-VMI": [1, 7],
            },
            "Gauss": {
                "Weapon_Gauss_Gauss_Silverbullet": [1, 2],
                "Weapon_Gauss_Heavy_0-STOCK": [1, 3],
                "Weapon_Gauss_ImprovedHeavy_0-STOCK": [1, 2],
                "Weapon_Gauss_Gauss_0-STOCK": [1, 5],
                "Weapon_Gauss_Gauss_1-M7": [1, 3],
                "Weapon_Gauss_Gauss_2-M9": [1, 2],
            },
            "Rifle": {
                "Weapon_Autocannon_HeavyRifle": [1, 6],
                "Weapon_Autocannon_MediumRifle": [1, 6],
                "Weapon_Autocannon_LightRifle": [1, 6]
            },
            "SRM": {
                "Weapon_SRM_SRM2_0-STOCK": [1, 8],
                "Weapon_SRM_SRM2_1-Holly": [1, 7],
                "Weapon_SRM_SRM2_1-Irian": [1, 7],
                "Weapon_SRM_SRM2_2-Holly": [1, 6],
                "Weapon_SRM_SRM2_2-Irian": [1, 6],
                "Weapon_SRM_SRM2_2-Valiant": [1, 6],
                "Weapon_SRM_SRM2_3-Valiant": [1, 5],
                "Weapon_SRM_SRM4_0-STOCK": [1, 8],
                "Weapon_SRM_SRM4_1-Holly": [1, 7],
                "Weapon_SRM_SRM4_1-Irian": [1, 7],
                "Weapon_SRM_SRM4_2-Holly": [1, 6],
                "Weapon_SRM_SRM4_2-Irian": [1, 6],
                "Weapon_SRM_SRM4_2-Valiant": [1, 6],
                "Weapon_SRM_SRM4_3-Valiant": [1, 6],
                "Weapon_SRM_SRM6_0-STOCK": [1, 8],
                "Weapon_SRM_SRM6_1-Holly": [1, 7],
                "Weapon_SRM_SRM6_1-Irian": [1, 7],
                "Weapon_SRM_SRM6_2-Holly": [1, 6],
                "Weapon_SRM_SRM6_2-Irian": [1, 6],
                "Weapon_SRM_SRM6_2-Valiant": [1, 5],
                "Weapon_SRM_SRM6_3-Valiant": [1, 5],
            },
            "StreakSRM": {
                "Weapon_SRM_SRM2_Streak": [1, 5],
                "Weapon_SRM_SRM6_Streak": [1, 5],
                "Weapon_SRM_SRM4_Streak": [1, 5],
            },
            "StreakLRM": {

            },
            "MRM": {
                "Weapon_MRM_MRM10": [1, 5],
                "Weapon_MRM_MRM20": [1, 5],
                "Weapon_MRM_MRM30": [1, 5],
                "Weapon_MRM_MRM40": [1, 5],
            },
            "LRM": {
                "Weapon_LRM_LRM5_0-STOCK": [1, 7],
                "Weapon_LRM_LRM5_1-Delta": [1, 6],
                "Weapon_LRM_LRM5_1-LongFire": [1, 6],
                "Weapon_LRM_LRM5_1-Telos": [1, 6],
                "Weapon_LRM_LRM5_2-Delta": [1, 5],
                "Weapon_LRM_LRM5_2-LongFire": [1, 5],
                "Weapon_LRM_LRM5_2-Telos": [1, 5],
                "Weapon_LRM_LRM5_2-Zeus": [1, 5],
                "Weapon_LRM_LRM5_3-Zeus": [1, 4],
                "Weapon_LRM_LRM10_0-STOCK": [1,7],
                "Weapon_LRM_LRM10_1-Delta": [1, 6],
                "Weapon_LRM_LRM10_1-LongFire": [1, 6],
                "Weapon_LRM_LRM10_1-Telos": [1, 6],
                "Weapon_LRM_LRM10_2-Delta": [1, 5],
                "Weapon_LRM_LRM10_2-LongFire": [1, 5],
                "Weapon_LRM_LRM10_2-Telos": [1, 5],
                "Weapon_LRM_LRM10_2-Zeus": [1, 5],
                "Weapon_LRM_LRM10_3-Zeus": [1, 4],
                "Weapon_LRM_LRM15_0-STOCK": [1, 7],
                "Weapon_LRM_LRM15_1-Delta": [1, 6],
                "Weapon_LRM_LRM15_1-LongFire": [1, 6],
                "Weapon_LRM_LRM15_1-Telos": [1, 6],
                "Weapon_LRM_LRM15_2-Delta": [1, 5],
                "Weapon_LRM_LRM15_2-LongFire": [1, 5],
                "Weapon_LRM_LRM15_2-Telos": [1, 5],
                "Weapon_LRM_LRM15_2-Zeus": [1, 5],
                "Weapon_LRM_LRM15_3-Zeus": [1, 4],
                "Weapon_LRM_LRM20_0-STOCK": [1, 7],
                "Weapon_LRM_LRM20_1-Delta": [1, 6],
                "Weapon_LRM_LRM20_1-LongFire": [1, 6],
                "Weapon_LRM_LRM20_1-Telos": [1, 6],
                "Weapon_LRM_LRM20_2-Delta": [1, 5],
                "Weapon_LRM_LRM20_2-LongFire": [1, 5],
                "Weapon_LRM_LRM20_2-Telos": [1, 5],
                "Weapon_LRM_LRM20_2-Zeus": [1, 5],
                "Weapon_LRM_LRM20_3-Zeus": [1, 4],
            },
            "TBOLT": {
                "Weapon_LRM_Thunderbolt5": [1, 5],
                "Weapon_LRM_Thunderbolt10": [1, 5],
                "Weapon_LRM_Thunderbolt15": [1, 4],
                "Weapon_LRM_Thunderbolt20": [1, 4],
            },
            "Artillery": {
                "Weapon_Mortar4": [1, 6],
                "Weapon_Mortar6": [1, 5],
                "Weapon_Mortar8": [1, 5],
                "Weapon_Autocannon_LONGTOM": [1, 3],
                "Weapon_Autocannon_SNIPER": [1, 3],
                "Weapon_Autocannon_THUMPER": [1, 3]
            },
            "Flamer": {
                "Weapon_Flamer_Flamer_0-STOCK": [1, 9],
                "Weapon_Flamer_Flamer_1-Hotshot": [1, 8],
                "Weapon_Flamer_Flamer_2-Olympus": [1, 8],
                "Weapon_Flamer_Flamer_SPECIAL-Victoria": [1, 7],
            },
            "Support": {
                "Weapon_Laser_AMS": [1, 2],
                "Weapon_AMS": [1, 6],
                "Weapon_TAG_Standard_0-STOCK": [1, 6],
                "Weapon_TAG_Standard_1-Mendham": [1, 5],
                "Weapon_TAG_Standard_2-Ceres_Arms": [1, 5],
                "Weapon_Narc_Standard_0-STOCK": [1, 6],
                "Weapon_Narc_Standard_1-Ceres_Arms": [1, 5],
                "Weapon_Narc_Standard_2-Kali_Yama": [1, 15],
            },
        },
        "AmmunitionBox": {
            "Ammo_Periphery": {
             "Ammo_AmmunitionBox_Rifle_L": [1, 7],
             "Ammo_AmmunitionBox_Rifle_M": [1, 6],
             "Ammo_AmmunitionBox_Rifle_H": [1, 5],
            },
            "Ammo_Common": {
                "Ammo_AmmunitionBox_Generic_MRM": [1, 5],
                "Ammo_AmmunitionBox_Generic_AC2": [1, 8],
                "Ammo_AmmunitionBox_Generic_AC5": [1, 8],
                "Ammo_AmmunitionBox_Generic_AC10": [1, 7],
                "Ammo_AmmunitionBox_Generic_AC20": [1, 7],
                "Ammo_AmmunitionBox_Generic_Flamer": [1, 8],
                "Ammo_AmmunitionBox_Generic_GAUSS": [1, 4],
                "Ammo_AmmunitionBox_Generic_Narc": [1, 5],
                "Ammo_AmmunitionBox_Generic_SRM": [1, 8]
            },
            "Ammo_CommonII": {
                "Ammo_AmmunitionBox_MachineGun": [1, 9],
                "Ammo_AmmunitionBox_AMS": [1, 6],
                "Ammo_AmmunitionBox_Generic_LB2X": [1, 5],
                "Ammo_AmmunitionBox_Generic_LB5X": [1, 5],
                "Ammo_AmmunitionBox_Generic_LB10X": [1, 4],
                "Ammo_AmmunitionBox_Generic_LB20X": [1, 4],
                "Ammo_AmmunitionBox_Generic_LRM": [1, 8]
            },
            "Ammo_Uncommon": {
                "Ammo_AmmunitionBox_HVAC2": [1, 4],
                "Ammo_AmmunitionBox_HVAC5": [1, 4],
                "Ammo_AmmunitionBox_HVAC10": [1, 3],
                "Ammo_AmmunitionBox_HVAC20": [1, 3],
                "Ammo_AmmunitionBox_TBOLT5": [1, 5],
                "Ammo_AmmunitionBox_TBOLT10": [1, 5],
                "Ammo_AmmunitionBox_TBOLT15": [1, 4],
                "Ammo_AmmunitionBox_TBOLT20": [1, 4],
                "Ammo_AmmunitionBox_Thumper": [1, 3],
                "Ammo_AmmunitionBox_Generic_UAC2": [1, 5],
                "Ammo_AmmunitionBox_Generic_UAC5": [1, 5],
                "Ammo_AmmunitionBox_Generic_UAC10": [1, 4],
                "Ammo_AmmunitionBox_Generic_UAC20": [1, 4],
                "Ammo_AmmunitionBox_ArrowIV": [1, 4]
            },
            "Ammo_Rare": {
                "Ammo_AmmunitionBox_SBGauss": [1, 2],
            },
            "Ammo_Special": {},
        }
    }
# NOTE: item_Collections switches to a different format due to item_Collections have mixed types in the CSV's. reference is used when calling another csv file, instead of a specific JSON
item_Collection = {
    "Ammo_all": {
     "GN_Ammo_Common": ["Reference",4, 5],
     "GN_Ammo_CommonII": ["Reference",4, 5],
     "GN_Ammo_Uncommon": ["Reference",2, 2],
     "GN_Ammo_Rare": ["Reference",1, 1]
     },  #StreamingAssets/data/itemCollections CSV's Below
    "Battlefield": {},
    "Industrial": {},
    "Research": {},
    "shop_research": {},
    "SLDF": {},
    "Smuggler": {},
    "shopItems_battlefield": {},
    "shopItems_battlefieldProgression": {},
    "shopItems_blackmarket": {},
    "shopItems_blackmarket_gaussandammo": {},
    "shopItems_blackmarket_narcandammo": {},
    "shopItems_chemicals": {},
    "shopItems_chemicalsProgression": {},
    "shopItems_electronics": {},
    "shopItems_electronicsProgression": {},
    "shopItems_manufacturing": {},
    "shopItems_manufacturingProgression": {},
    "shopItems_mining": {},
    "shopItems_miningProgression": {},
    "shopItems_munitions": {},
    "shopItems_munitionsProgression": {},
    "shopItems_research": {},
    "shopItems_researchProgression": {},
    "shopItems_starleague": {},
    "shopItems_starleagueProgression": {},
    "shopItems_weapons": {},
    "MechParts_Davion_rare": {},
    "MechParts_Davion_uncommon": {},
    "MechParts_Kurita_rare": {},
    "MechParts_Liao_rare": {},
    "MechParts_SLDF": {},
    "MechParts_Steiner_rare": {},  #------------------------------------MechParts------------------------------------
    "systemStores_MechParts_BlackMarket_Assault": {
    "mechdef_stalker_STK-4N": ["MechPart",1, 4]
    },
    "systemStores_MechParts_common_Assault": {
    "mechdef_atlas_AS7-D": ["MechPart",1, 2]
    },
    "systemStores_MechParts_common_Heavy": {
    "mechdef_quickdraw_QKD-5A": ["MechPart",1, 6]
    },
    "systemStores_MechParts_common_Light": {
    "mechdef_urbanmech_UM-R60": ["MechPart",1, 8]
    },
    "systemStores_MechParts_common_Medium": {
    "mechdef_shadowhawk_SHD-2H": ["MechPart",1, 7]
    },
    "systemStores_MechParts_Davion_Assault": {
    "mechdef_banshee_BNC-3S": ["MechPart",1, 2]
    },
    "systemStores_MechParts_Davion_Heavy": {
    "mechdef_thunderbolt_TDR-5D": ["MechPart",1, 6]
    },
    "systemStores_MechParts_Davion_Light": {
    "mechdef_panther_PNT-9R": ["MechPart",1, 8]
    },
    "systemStores_MechParts_Davion_Medium": {
    "mechdef_phoenixhawk_PXH-1D": ["MechPart",1, 7]
    },
    "systemStores_MechParts_Directorate_Assault": {
    "mechdef_banshee_BNC-3S": ["MechPart",1, 2]
    },
    "systemStores_MechParts_Directorate_Heavy": {
    "mechdef_grasshopper_GHR-5H": ["MechPart",1, 6]
    },
    "systemStores_MechParts_Directorate_Light": {
    "mechdef_urbanmech_UM-R90": ["MechPart",1, 8]
    },
    "systemStores_MechParts_Directorate_Medium": {
    "mechdef_hunchback_HBK-4J": ["MechPart",1, 7]
    },
    "systemStores_MechParts_Kurita_Assault": {
    "mechdef_hatamoto-Kaze_HTM-27V": ["MechPart",1, 2]
    },
    "systemStores_MechParts_Kurita_Heavy": {
    "mechdef_catapult_CPLT-K3": ["MechPart",1, 6]
    },
    "systemStores_MechParts_Kurita_Light": {
    "mechdef_Hermes_HER-1B": ["MechPart",1, 8]
    },
    "systemStores_MechParts_Kurita_Medium": {
    "mechdef_dragon_DRG-1C": ["MechPart",1, 7]
    },
    "systemStores_MechParts_Liao_Assault": {
    "mechdef_atlas_AS7-A": ["MechPart",1, 2]
    },
    "systemStores_MechParts_Liao_Heavy": {
    "mechdef_cataphract_CTF-4X": ["MechPart",1, 6]
    },
    "systemStores_MechParts_Liao_Light": {
    "mechdef_raven_RVN-3L": ["MechPart",1, 8]
    },
    "systemStores_MechParts_Liao_Medium": {
    "mechdef_vindicator_VND-1R": ["MechPart",1, 7]
    },
    "systemStores_MechParts_Magistracy_Assault": {
    "mechdef_atlas_AS7-RS": ["MechPart",1, 2]
    },
    "systemStores_MechParts_Magistracy_Heavy": {
    "mechdef_orion_ON1-K": ["MechPart",1, 6]
    },
    "systemStores_MechParts_Magistracy_Light": {
    "mechdef_Ostscout-OTT7J": ["MechPart",1, 8]
    },
    "systemStores_MechParts_Magistracy_Medium": {
    "mechdef_Wyvern_WVE-6N": ["MechPart",1, 7]
    },
    "systemStores_MechParts_Marik_Assault": {
    "mechdef_banshee_BNC-3M": ["MechPart",1, 2]
    },
    "systemStores_MechParts_Marik_Heavy": {
    "mechdef_warhammer_WHM-7M": ["MechPart",1, 6]
    },
    "systemStores_MechParts_Marik_Light": {
    "mechdef_flea_FLE-15": ["MechPart",1, 8]
    },
    "systemStores_MechParts_Marik_Medium": {
    "mechdef_phoenixhawk_PXH-3M": ["MechPart",1, 7]
    },
    "systemStores_MechParts_Steiner_Assault": {
    "mechdef_battlemaster_BLR-1S": ["MechPart",1, 2]
    },
    "systemStores_MechParts_Steiner_Heavy": {
    "mechdef_archer_ARC-2S": ["MechPart",1, 6]
    },
    "systemStores_MechParts_Steiner_Light": {
    "mechdef_locust_LCT-1S": ["MechPart",1, 8]
    },
    "systemStores_MechParts_Steiner_Medium": {
    "mechdef_enforcer_ENF-4R": ["MechPart",1, 7]
    },
    "systemStores_MechParts_Taurian_Assault": {
    "mechdef_battlemaster_BLR-1G": ["MechPart",1, 2]
    },
    "systemStores_MechParts_Taurian_Heavy": {
    "mechdef_archer_ARC-2R": ["MechPart",1, 6]
    },
    "systemStores_MechParts_Taurian_Light": {
    "mechdef_locust_LCT-3V": ["MechPart",1, 8]
    },
    "systemStores_MechParts_Taurian_Medium": {
    "mechdef_hunchback_HBK-4H": ["MechPart",1, 7]
    },
    "Periphery_Light_Mech_Parts": {
    "mechdef_Clint_CLNT-1-2R": ["MechPart",1,3],
    "mechdef_falcon_FLC-4N": ["MechPart",1,4],
    "mechdef_Hermes_HER-1A": ["MechPart",1,3],
    "mechdef_Hornet_HNT-151": ["MechPart",1,1],
    "mechdef_locust_LCT-1M": ["MechPart",1,5]
},
"Periphery_Medium_Mech_Parts": {
    "mechdef_shadowhawk_SHD-2H": ["MechPart",1,2],
    "mechdef_wolverine_WVR-6M": ["MechPart",1,3],
    "mechdef_blackjack_BJ-1": ["MechPart",1,3],
    "mechdef_phoenixhawk_PXH-1": ["MechPart",1,2]
},
"Periphery_Heavy_Mech_Parts": {
    "mechdef_Ostroc_OSR-3C": ["MechPart",1,2],
    "mechdef_crusader_CRD-3R": ["MechPart",1,1],
    "mechdef_Ostsol_OTL-4D": ["MechPart",1,2],
    "mechdef_quickdraw_QKD-4H": ["MechPart",1,3]
},
"InnerSphere_Light_Mech_Parts": {
    "mechdef_Clint_CLNT-2-4T": ["MechPart",1,4],
    "mechdef_commando_COM-1D": ["MechPart",1,5],
    "mechdef_commando_COM-2D": ["MechPart",1,4],
    "mechdef_falcon_FLC-4N": ["MechPart",1,6]
},
"InnerSphere_Medium_Mech_Parts": {
    "mechdef_raven_RVN-3L": ["MechPart",1,2],
    "mechdef_dervish_DV-6M": ["MechPart",1,4],
    "mechdef_phoenixhawk_PXH-1": ["MechPart",1,3],
    "mechdef_Chameleon_TRC-4B": ["MechPart",1,4]
},
"InnerSphere_Heavy_Mech_Parts": {
    "mechdef_marauder_MAD-3R": ["MechPart",1,2],
    "mechdef_thunderbolt_TDR-5S": ["MechPart",1,4],
    "mechdef_orion_ON1-K": ["MechPart",1,3],
    "mechdef_orion_ON1-V": ["MechPart",1,2]
},
"ComStar_Light_Mech_Parts": {
    "mechdef_firefly_FFL-4C": ["MechPart",1,4],
    "mechdef_hussar_HSR-200-D": ["MechPart",1,5],
    "mechdef_thorn_THE-N": ["MechPart",1,4],
    "mechdef_Hermes_HER-1S": ["MechPart",1,6]
},
"ComStar_Medium_Mech_Parts": {
    "mechdef_Sentinel_STN-3L": ["MechPart",1,2],
    "mechdef_Crab_CRB-27": ["MechPart",1,4],
    "mechdef_Kintaro_KTO-19": ["MechPart",1,3],
    "mechdef_assassin_ASN-21": ["MechPart",1,4]
},
"ComStar_Heavy_Mech_Parts": {
    "mechdef_champion_CHP-1N": ["MechPart",1,2],
    "mechdef_exterminator_EXT-4D": ["MechPart",1,4],
    "mechdef_marauder_MAD-1R": ["MechPart",1,3],
    "mechdef_thug_THG-11E": ["MechPart",1,2]
},
    "Clan_Light_Mech_Parts": {},
    "Clan_Medium_Mech_Parts": {},
    "Clan_Heavy_Mech_Parts": {},
    
    
    "ComStar_Light_Tanks": {}, #------------------------------------Tank Parts------------------------------------
    "ComStar_Medium_Tanks": {},
    "ComStar_Heavy_Tanks": {},
    "Periphery_Light_Tanks": {},
    "Periphery_Medium_Tanks": {},
    "Periphery_Heavy_Tanks": {},
    "InnerSphere_Light_Tanks": {},
    "InnerSphere_Medium_Tanks": {},
    "InnerSphere_Heavy_Tanks": {},
    "Clan_Light_Tanks": {},
    "Clan_Medium_Tanks": {},
    "Clan_Heavy_Tanks": {},
    "ComStar_Light_Tank_Parts": {},
    "ComStar_Medium_Tank_Parts": {},
    "ComStar_Heavy_Tank_Parts": {},
    "Periphery_Light_Tank_Parts": {},
    "Periphery_Medium_Tank_Parts": {},
    "Periphery_Heavy_Tank_Parts": {},
    "InnerSphere_Light_Tank_Parts": {},
    "InnerSphere_Medium_Tank_Parts": {},
    "InnerSphere_Heavy_Tank_Parts": {},
    "Clan_Light_Tank_Parts": {},
    "Clan_Medium_Tank_Parts": {},
    "Clan_Heavy_Tank_Parts": {},
    "systemStores_Mechs_BlackMarket_Assault": {
        "mechdef_awesome_AWS-8Q": ["Mech", 1, 2]  #------------------------------------Mechs------------------------------------
    },
    "systemStores_Mechs_common_Assault": {
        "mechdef_orion_ON1-V": ["Mech", 1, 2]
    },
    "systemStores_Mechs_common_Heavy": {
        "mechdef_rifleman_RFL-3N": ["Mech", 1, 2]
    },
    "systemStores_Mechs_common_Light": {
        "mechdef_locust_LCT-1V": ["Mech", 1, 2]
    },
    "systemStores_Mechs_common_Medium": {
        "mechdef_cicada_CDA-2A": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Davion_Assault": {
        "mechdef_locust_LCT-3V": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Davion_Heavy": {
        "mechdef_zeus_ZEU-6A": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Davion_Light": {
        "mechdef_locust_LCT-1M": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Davion_Medium": {
        "mechdef_hatchetman_HCT-3F": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Directorate_Assault": {
        "mechdef_victor_VTR-9B": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Directorate_Heavy": {
        "mechdef_warhammer_WHM-6R": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Directorate_Light": {
        "mechdef_spider_SDR-5D": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Directorate_Medium": {
        "mechdef_blackjack_BJ-1V": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Kurita_Assault": {
        "mechdef_mauler_MAL-1R": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Kurita_Heavy": {
        "mechdef_archer_ARC-2K": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Kurita_Light": {
        "mechdef_falcon_FLC-4N": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Kurita_Medium": {
        "mechdef_HermesII_HER-4K": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Liao_Assault": {
        "mechdef_highlander_HGN-733C": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Liao_Heavy": {
        "mechdef_marauder_MAD-3L": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Liao_Light": {
        "mechdef_locust_LCT-1L": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Liao_Medium": {
        "mechdef_raven_RVN-1X": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Magistracy_Assault": {
        "mechdef_awesome_AWS-8V": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Magistracy_Heavy": {
        "mechdef_crusader_CRD-3R": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Magistracy_Light": {
        "mechdef_jenner_JR7-D": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Magistracy_Medium": {
        "mechdef_Chameleon_TRC-4B": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Marik_Assault": {
        "mechdef_atlas_AS7-A": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Marik_Heavy": {
        "mechdef_marauder_MAD-3M": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Marik_Light": {
        "mechdef_Hermes_HER-3S": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Marik_Medium": {
        "mechdef_HermesII_HER-2M": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Steiner_Assault": {
        "mechdef_highlander_HGN-733C": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Steiner_Heavy": {
        "mechdef_thunderbolt_TDR-5SS": ["Mech", 1, 2]
    },
     "systemStores_Mechs_Steiner_Light": {
        "mechdef_Wolfhound_WLF-1A": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Steiner_Medium": {
        "mechdef_Sentinel_STN-3KA": ["Mech", 1, 2],
    },
    "systemStores_Mechs_Taurian_Assault": {
        "mechdef_stalker_STK-3H": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Taurian_Heavy": {
        "mechdef_quickdraw_QKD-5A": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Taurian_Light": {
        "mechdef_javelin_JVN-10N": ["Mech", 1, 2]
    },
    "systemStores_Mechs_Taurian_Medium": {
        "mechdef_trebuchet_TBT-5N": ["Mech", 1, 2]
        },
    "ComStar_Light_Mechs": {
        "mechdef_hussar_HSR-200-D": ["Mech", 1, 5],
        "mechdef_firefly_FFL-4C": ["Mech", 1, 6]
    },
    "ComStar_Medium_Mechs": {
        "mechdef_Sentinel_STN-3L": ["Mech", 1, 5],
        "mechdef_Crab_CRB-27": ["Mech", 1, 6]
},
"ComStar_Heavy_Mechs": {
    "mechdef_exterminator_EXT-4D": ["Mech", 1, 5],
    "mechdef_lancelot_LNC25-01": ["Mech", 1, 6]
},
"Periphery_Light_Mechs": {
    "mechdef_Ostscout-OTT7J": ["Mech", 1, 1],
    "mechdef_jenner_JR7-F": ["Mech", 1, 1],
    "mechdef_firestarter_FS9-H": ["Mech", 1, 1],
    "mechdef_javelin_JVN-10A": ["Mech", 1, 1]
},
"Periphery_Medium_Mechs": {
    "mechdef_Whitworth_WTH-1": ["Mech", 1, 1],
    "mechdef_hunchback_HBK-4N": ["Mech", 1, 1],
    "mechdef_enforcer_ENF-4R": ["Mech", 1, 1],
    "mechdef_centurion_CN9-AL": ["Mech", 1, 1]
},
"Periphery_Heavy_Mechs": {
    "mechdef_thunderbolt_TDR-5S": ["Mech", 1, 1],
    "mechdef_rifleman_RFL-3N": ["Mech", 1, 1],
    "mechdef_catapult_CPLT-C1": ["Mech", 1, 1],
    "mechdef_grasshopper_GHR-5H": ["Mech", 1, 1]
},
"InnerSphere_Light_Mechs": {
    "mechdef_javelin_JVN-10N": ["Mech", 1, 1],
    "mechdef_spider_SDR-5V": ["Mech", 1, 1],
    "mechdef_locust_LCT-1V": ["Mech", 1, 1],
    "mechdef_jenner_JR7-D": ["Mech", 1, 1]
},
"InnerSphere_Medium_Mechs": {
    "mechdef_Whitworth_WTH-1": ["Mech", 1, 1],
    "mechdef_hunchback_HBK-4N": ["Mech", 1, 1],
    "mechdef_kintaro_KTO-18": ["Mech", 1, 1],
    "mechdef_centurion_CN9-A": ["Mech", 1, 1]
},
"InnerSphere_Heavy_Mechs": {
    "mechdef_quickdraw_QKD-5A": ["Mech", 1, 1],
    "mechdef_warhammer_WHM-6R": ["Mech", 1, 1],
    "mechdef_orion_ON1-K": ["Mech", 1, 1],
    "mechdef_griffin_GRF-1N": ["Mech", 1, 1]
},
"Clan_Light_Mechs": {},
"Clan_Medium_Mechs": {},
"Clan_Heavy_Mechs": {},#------------------------------------Weapon Collections------------------------------------
    "Weapons_common": {
                "Weapon_Laser_LargeLaser_0-STOCK": ["Weapon",1, 8],
                "Weapon_Laser_LargeLaser_1-Diverse_Optics": ["Weapon",1, 5],
                "Weapon_Laser_LargeLaser_1-ExoStar": ["Weapon",1, 5],
                "Weapon_Laser_LargeLaser_1-Intek": ["Weapon",1, 5],
                "Weapon_Laser_MediumLaser_0-STOCK": ["Weapon",1, 8],
                "Weapon_Laser_MediumLaser_1-ExoStar": ["Weapon",1, 5],
                "Weapon_Laser_MediumLaser_1-Intek": ["Weapon",1, 5],
                "Weapon_Laser_MediumLaser_1-Magna": ["Weapon",1, 5],
                "Weapon_Laser_SmallLaser_0-STOCK": ["Weapon",1, 8],
                "Weapon_Laser_SmallLaser_1-Diverse_Optics": ["Weapon",1, 5],
                "Weapon_Laser_SmallLaser_1-ExoStar": ["Weapon",1, 5],
                "Weapon_Laser_SmallLaser_1-Magna": ["Weapon",1, 5],
                "Weapon_PPC_PPCSnub_0-STOCK": ["Weapon",1, 6],
                "Weapon_PPC_PPCSnub_1-Ceres_Arms": ["Weapon",1, 6],
                "Weapon_PPC_PPCSnub_1-Donal": ["Weapon",1, 6],
                "Weapon_PPC_PPCSnub_1-Magna": ["Weapon",1, 6],
                "Weapon_PPC_PPC_0-STOCK": ["Weapon",1, 7],
                "Weapon_PPC_PPC_1-Ceres_Arms": ["Weapon",1, 6],
                "Weapon_PPC_PPC_1-Donal": ["Weapon",1, 6],
                "Weapon_PPC_PPC_1-Tiegart": ["Weapon",1, 6],
                "Weapon_Autocannon_AC2_0-STOCK": ["Weapon",1, 8],
                "Weapon_Autocannon_AC2_1-Defiance": ["Weapon",1, 7],
                "Weapon_Autocannon_AC2_1-Federated": ["Weapon",1, 7],
                "Weapon_Autocannon_AC2_1-Kali_Yama": ["Weapon",1, 7],
                "Weapon_Autocannon_AC10_0-STOCK": ["Weapon",1, 7],
                "Weapon_Autocannon_AC10_1-Defiance": ["Weapon",1, 6],
                "Weapon_Autocannon_AC10_1-Imperator": ["Weapon",1, 6],
                "Weapon_Autocannon_AC10_1-Kali_Yama": ["Weapon",1, 6],
                "Weapon_Autocannon_AC10_1-Mydron": ["Weapon",1, 6],
                "Weapon_Autocannon_AC5_1-Defiance": ["Weapon",1, 7],
                "Weapon_Autocannon_AC5_1-Federated": ["Weapon",1, 7],
                "Weapon_Autocannon_AC5_1-Imperator": ["Weapon",1, 7],
                "Weapon_Autocannon_AC5_1-Kali_Yama": ["Weapon",1, 7],
                "Weapon_Autocannon_AC20_1-Defiance": ["Weapon",1, 6],
                "Weapon_Autocannon_AC20_1-Federated": ["Weapon",1, 6],
                "Weapon_Autocannon_AC20_1-Imperator": ["Weapon",1, 6],
                "Weapon_Autocannon_AC20_1-Mydron": ["Weapon",1, 6],
                "Weapon_MachineGun_MachineGun_0-STOCK": ["Weapon",1, 9],
                "Weapon_MachineGun_MachineGun_1-Brigadier": ["Weapon",1, 8],
                "Weapon_MachineGun_MachineGun_1-VMI": ["Weapon",1, 8],
                "Weapon_SRM_SRM2_0-STOCK": ["Weapon",1, 8],
                "Weapon_SRM_SRM2_1-Holly": ["Weapon",1, 7],
                "Weapon_SRM_SRM4_0-STOCK": ["Weapon",1, 8],
                "Weapon_SRM_SRM4_1-Holly": ["Weapon",1, 7],
                "Weapon_SRM_SRM6_0-STOCK": ["Weapon",1, 8],
                "Weapon_SRM_SRM6_1-Holly": ["Weapon",1, 7],
                "Weapon_LRM_LRM5_0-STOCK": ["Weapon",1, 7],
                "Weapon_LRM_LRM5_1-Delta": ["Weapon",1, 6],
                "Weapon_LRM_LRM10_0-STOCK": ["Weapon",1,7],
                "Weapon_LRM_LRM10_1-Delta": ["Weapon",1, 6],
                "Weapon_LRM_LRM15_0-STOCK": ["Weapon",1, 7],
                "Weapon_LRM_LRM15_1-Delta": ["Weapon",1, 6],
                "Weapon_LRM_LRM20_0-STOCK": ["Weapon",1, 7],
                "Weapon_LRM_LRM20_1-Delta": ["Weapon",1, 6],
                "Weapon_Flamer_Flamer_0-STOCK": ["Weapon",1, 9],
                "Weapon_Flamer_Flamer_1-Hotshot": ["Weapon",1, 8],
                "Weapon_AMS": ["Weapon",1, 6],
                "Weapon_TAG_Standard_0-STOCK": ["Weapon",1, 6],
                "Weapon_TAG_Standard_1-Mendham": ["Weapon",1, 5],
                "Weapon_TAG_Standard_2-Ceres_Arms": ["Weapon",1, 5],
                "Weapon_Narc_Standard_0-STOCK": ["Weapon",1, 6],
                "Weapon_Narc_Standard_1-Ceres_Arms": ["Weapon",1, 5],
                "Weapon_Gauss_Gauss_0-STOCK": ["Weapon",1, 5]
    },
     "Weapons_uncommon": {
                "Weapon_Autocannon_UAC2_0-STOCK": ["Weapon",1, 5],
                "Weapon_Autocannon_UAC2_1-Imperator": ["Weapon",1, 4],
                "Weapon_Autocannon_UAC5_0-STOCK": ["Weapon",1, 5],
                "Weapon_Autocannon_UAC5_1-Mydron": ["Weapon",1, 4],
                "Weapon_Autocannon_UAC10_0-STOCK": ["Weapon",1, 5],
                "Weapon_Autocannon_UAC10_1-Federated": ["Weapon",1, 4],
                "Weapon_Autocannon_UAC20_0-STOCK": ["Weapon",1, 5],
                "Weapon_Autocannon_UAC20_1-Kali_Yama": ["Weapon",1, 4],
                "Weapon_Autocannon_LB2X_0-STOCK": ["Weapon",1, 6],
                "Weapon_Autocannon_LB2X_1-Defiance": ["Weapon",1, 5],
                "Weapon_Autocannon_LB5X_0-STOCK": ["Weapon",1, 6],
                "Weapon_Autocannon_LB5X_1-GM": ["Weapon",1, 5],
                "Weapon_Autocannon_LB10X_0-STOCK": ["Weapon",1, 6],
                "Weapon_Autocannon_LB10X_1-Western": ["Weapon",1, 5],
                "Weapon_Autocannon_LB20X_0-STOCK": ["Weapon",1, 6],
                "Weapon_Autocannon_LB20X_1-Shengli_Arms": ["Weapon",1, 5],
                "Weapon_Autocannon_HeavyRifle": ["Weapon",1, 6],
                "Weapon_Autocannon_MediumRifle": ["Weapon",1, 6],
                "Weapon_Autocannon_LightRifle": ["Weapon",1, 6],
                "Weapon_MRM_MRM10": ["Weapon",1, 5],
                "Weapon_MRM_MRM20": ["Weapon",1, 5],
                "Weapon_MRM_MRM30": ["Weapon",1, 5],
                "Weapon_MRM_MRM40": ["Weapon",1, 5],
                "Weapon_LRM_Thunderbolt5": ["Weapon",1, 5],
                "Weapon_LRM_Thunderbolt10": ["Weapon",1, 5],
                "Weapon_LRM_Thunderbolt15": ["Weapon",1, 4],
                "Weapon_LRM_Thunderbolt20": ["Weapon",1, 4],
                "Weapon_Mortar4": ["Weapon",1, 3],
                "Weapon_Mortar6": ["Weapon",1, 3],
                "Weapon_Mortar8": ["Weapon",1, 3],
                "Weapon_Autocannon_LONGTOM": ["Weapon",1, 1],
                "Weapon_Autocannon_SNIPER": ["Weapon",1, 1],
                "Weapon_Autocannon_THUMPER": ["Weapon",1, 1],
                "Weapon_Gauss_Gauss_1-M7": ["Weapon",1, 3],
                "Weapon_Gauss_Gauss_2-M9": ["Weapon",1, 2]
    },
    "Weapons_rare": {
                "Weapon_Autocannon_HVAC2_0-STOCK": ["Weapon",1, 3],
                "Weapon_Autocannon_HVAC5_0-STOCK": ["Weapon",1, 3],
                "Weapon_Autocannon_HVAC10_0-STOCK": ["Weapon",1, 3],
                "Weapon_Autocannon_HVAC20_0-STOCK": ["Weapon",1, 3],
                "Weapon_Laser_AMS": ["Weapon",1, 2],
                "Weapon_Gauss_Gauss_Silverbullet": ["Weapon",1, 2],
                "Weapon_Gauss_Heavy_0-STOCK": ["Weapon",1, 3],
                "Weapon_Gauss_ImprovedHeavy_0-STOCK": ["Weapon",1, 2]
    },
     #------------------------------------Upgrade Collections------------------------------------
"HighEndEngines": {
    "emod_engine_350": ["HeatSink", 1, 3],
    "emod_engine_355": ["HeatSink", 1, 4],
    "emod_engine_360": ["HeatSink", 1, 5],
    "emod_engine_365": ["HeatSink", 1, 7],
    "emod_engine_370": ["HeatSink", 1, 7],
    "emod_engine_375": ["HeatSink", 1, 7],
    "emod_engine_380": ["HeatSink", 1, 7],
    "emod_engine_390": ["HeatSink", 1, 7],
    "emod_engine_395": ["HeatSink", 1, 5],
    "emod_engine_400": ["HeatSink", 1, 4]
},
    "EquipmentCommon": {
    "GN_HeatSinks-T1": ["Reference",5,7],
    "GN_Engines-T1": ["Reference",1,5],
    "GN_Structure-T1": ["Reference",1,5],
    "GN_Armor-T1": ["Reference",1,5],
    "GN_JumpJets": ["Reference",10,6]
    },
    "EquipmentUncommon": {
    "GN_Armor-T2": ["Reference",1,5],
    "GN_Actuators": ["Reference",1,3],
    "GN_Structure-T1": ["Reference",1,6],
    "GN_Cockpit": ["Reference",1,6],
    "GN_Life_Support": ["Reference",2,5],
    "GN_HeatSinks-T1": ["Reference",4,8],
    "GN_HSKits": ["Reference",1,5]
    },
    "EquipmentRare": {
    "GN_Actuators": ["Reference",1,4],
    "GN_Structure-T2": ["Reference",1,7],
    "GN_Cockpit": ["Reference",1,7],
    "GN_Life_Support": ["Reference",2,8],
    "GN_ECM": ["Reference",1,5],
    "GN_HSKits": ["Reference",1,5],
    "GN_Gyro": ["Reference",1,6],
    "GN_Upgrades": ["Reference",2,3],
    "GN_Engines-T2": ["Reference",1,5],
    "GN_HeatSinks-T2": ["Reference",2,4]
    },
    "EquipmentPeripheryCommon": {
    "GN_Engines-T1": ["Reference",1,5],
    "GN_HeatSinks-T1": ["Reference",4,8],
    "GN_JumpJets": ["Reference",10,6],
    "GN_Structure-T1": ["Reference",1,5],
    "GN_Armor-T1": ["Reference",1,5]
    },
    "EquipmentPeripheryUncommon": {
    "GN_Cockpit": ["Reference",1,6],
    "GN_Life_Support": ["Reference",2,5],
    "GN_HSKits": ["Reference",1,5],
    "GN_Armor-T2": ["Reference",1,5]
    },
    "EquipmentPeripheryRare": {
    "GN_Gyro": ["Reference",1,6],
    "GN_Upgrades": ["Reference",2,5],
    "GN_HeatSinks-T2": ["Reference",2,1],
    "GN_Actuators": ["Reference",1,4],
    "GN_ECM": ["Reference",1,1],
    },
    "Weapons_Periphery": {
    "GN_Lasers": ["Reference",1,6],
    "GN_PPC": ["Reference",1,4],
    "GN_Autocannon": ["Reference",1,6],
    "GN_Autocannon_Large": ["Reference",1,6],
    "GN_MachineGun": ["Reference",1,8],
    "GN_SRM": ["Reference",1,7],
    "GN_LRM": ["Reference",1,7],
    "GN_Flamer": ["Reference",1,6],
    "GN_Rifle": ["Reference",1,9]
    },
    "Liked_InnerSphere": {
                "itemCollection_Weapons_common": ["Reference",3, 5],
                "itemCollection_Weapons_uncommon": ["Reference",2, 3],
                "itemCollection_Weapons_rare": ["Reference",1, 2],
                "itemCollection_EquipmentCommon": ["Reference",2, 2],
                "itemCollection_ComStar_Medium_Mech_Parts": ["Reference",2, 5],
                "itemCollection_ComStar_Light_Mech_Parts": ["Reference",2, 5]             
    },
    "Liked_Periphery": {
                "itemCollection_Weapons_Periphery": ["Reference",3, 8],
                "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
                "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
                "itemCollection_EquipmentPeripheryRare": ["Reference",1, 2],
                "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 5],
                "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 5]                    
    },
    "Liked_Clans": {},
    #------------------------------------Faction Lists------------------------------------NOTE: faction_ list cannot use reference list. I needs to be correct DEF Type
    "faction_ComStar": {},
    "Honored_ComStar": {
                "itemCollection_ComStar_Heavy_Mech_Parts": ["Reference",1, 3],
                "itemCollection_ComStar_Medium_Mech_Parts": ["Reference",1, 4],
                "itemCollection_ComStar_Light_Mech_Parts": ["Reference",1, 7],
                "itemCollection_Weapons_rare": ["Reference",2, 6],
                "itemCollection_EquipmentCommon": ["Reference",2, 8],
                "itemCollection_ComStar_Heavy_Mechs": ["Reference",1, 5]
                },
    "major_ComStar": {
                "GN_Ammo_Common": ["Reference",2, 1],
                "GN_Ammo_CommonII": ["Reference",2, 1],
                "itemCollection_HighEndEngines": ["Reference",2, 7],
                "itemCollection_Weapons_common": ["Reference",2, 6],
                "itemCollection_Weapons_uncommon": ["Reference",2, 6],
                "itemCollection_EquipmentRare": ["Reference",2, 4],
                "itemCollection_EquipmentUncommon": ["Reference",2, 5],
                "itemCollection_EquipmentCommon": ["Reference",2, 8],
                "itemCollection_ComStar_Medium_Mech_Parts": ["Reference",2, 5],
                "itemCollection_ComStar_Medium_Mechs": ["Reference",2, 5]                
    },
    "minor_ComStar": {
                "GN_Ammo_Common": ["Reference",2, 1],
                "GN_Ammo_CommonII": ["Reference",2, 1],
                "GN_EngineCore": ["Reference",3, 1],
                "itemCollection_Weapons_common": ["Reference",4, 6],
                "itemCollection_Weapons_uncommon": ["Reference",2, 6],
                "itemCollection_EquipmentUncommon": ["Reference",1, 5],
                "itemCollection_EquipmentCommon": ["Reference",2, 8]
    },
    
    "faction_Davion": {},
    "Honored_Davion": {},
    "major_Davion":{
        "GN_Ammo_Common": ["Reference",2, 1],
        "GN_Ammo_CommonII": ["Reference",2, 1],
        "itemCollection_HighEndEngines": ["Reference",2, 7],
        "itemCollection_Weapons_common": ["Reference",2, 6],
        "itemCollection_Weapons_uncommon": ["Reference",2, 6],
        "itemCollection_EquipmentRare": ["Reference",2, 4],
        "itemCollection_EquipmentUncommon": ["Reference",2, 5],
        "itemCollection_EquipmentCommon": ["Reference",2, 8],
        "itemCollection_InnerSphere_Medium_Mech_Parts": ["Reference",2, 5],
        "itemCollection_InnerSphere_Medium_Mechs": ["Reference",2, 5],
        "GN_Ammo_CommonII": ["Reference",2, 1],
        "itemCollection_HighEndEngines": ["Reference",2, 7],
        "itemCollection_Weapons_common": ["Reference",2, 6],
        "itemCollection_Weapons_uncommon": ["Reference",2, 6],
        "itemCollection_EquipmentRare": ["Reference",2, 4],
        "itemCollection_EquipmentUncommon": ["Reference",2, 5],
        "itemCollection_EquipmentCommon": ["Reference",2, 8],
        "itemCollection_InnerSphere_Medium_Mech_Parts": ["Reference",2, 5],
        "itemCollection_InnerSphere_Medium_Mechs": ["Reference",2, 5]  
    },
    "minor_Davion": {
                "GN_Ammo_Common": ["Reference",2, 1],
                "GN_Ammo_CommonII": ["Reference",2, 1],
                "GN_EngineCore": ["Reference",3, 1],
                "itemCollection_Weapons_common": ["Reference",4, 6],
                "itemCollection_Weapons_uncommon": ["Reference",2, 6],
                "itemCollection_EquipmentUncommon": ["Reference",1, 5],
                "itemCollection_EquipmentCommon": ["Reference",2, 8]
    },

    "faction_Steiner": {},
    "Honored_Steiner": {},
    "major_Steiner":{
        "GN_Ammo_Common": ["Reference",2, 1],
        "GN_Ammo_CommonII": ["Reference",2, 1],
        "itemCollection_HighEndEngines": ["Reference",2, 7],
        "itemCollection_Weapons_common": ["Reference",2, 6],
        "itemCollection_Weapons_uncommon": ["Reference",2, 6],
        "itemCollection_EquipmentRare": ["Reference",2, 4],
        "itemCollection_EquipmentUncommon": ["Reference",2, 5],
        "itemCollection_EquipmentCommon": ["Reference",2, 8],
        "itemCollection_InnerSphere_Medium_Mech_Parts": ["Reference",2, 5],
        "itemCollection_InnerSphere_Medium_Mechs": ["Reference",2, 5]
    },
    "minor_Steiner": {
                "GN_Ammo_Common": ["Reference",2, 1],
                "GN_Ammo_CommonII": ["Reference",2, 1],
                "GN_EngineCore": ["Reference",3, 1],
                "itemCollection_Weapons_common": ["Reference",4, 6],
                "itemCollection_Weapons_uncommon": ["Reference",2, 6],
                "itemCollection_EquipmentUncommon": ["Reference",1, 5],
                "itemCollection_EquipmentCommon": ["Reference",2, 8]
    },

    "faction_Liao": {},
    "Honored_Liao": {},
    "major_Liao":{
        "GN_Ammo_Common": ["Reference",2, 1],
        "GN_Ammo_CommonII": ["Reference",2, 1],
        "itemCollection_HighEndEngines": ["Reference",2, 7],
        "itemCollection_Weapons_common": ["Reference",2, 6],
        "itemCollection_Weapons_uncommon": ["Reference",2, 6],
        "itemCollection_EquipmentRare": ["Reference",2, 4],
        "itemCollection_EquipmentUncommon": ["Reference",2, 5],
        "itemCollection_EquipmentCommon": ["Reference",2, 8],
        "itemCollection_InnerSphere_Medium_Mech_Parts": ["Reference",2, 5],
        "itemCollection_InnerSphere_Medium_Mechs": ["Reference",2, 5]
    },
    "minor_Liao": {
            "GN_Ammo_Common": ["Reference",2, 1],
                "GN_Ammo_CommonII": ["Reference",2, 1],
                "GN_EngineCore": ["Reference",3, 1],
                "itemCollection_Weapons_common": ["Reference",4, 6],
                "itemCollection_Weapons_uncommon": ["Reference",2, 6],
                "itemCollection_EquipmentUncommon": ["Reference",1, 5],
                "itemCollection_EquipmentCommon": ["Reference",2, 8]
    },

    "faction_Kurita": {},
    "Honored_Kurita": {},
    "major_Kurita":{
        "GN_Ammo_Common": ["Reference",2, 1],
        "GN_Ammo_CommonII": ["Reference",2, 1],
        "itemCollection_HighEndEngines": ["Reference",2, 7],
        "itemCollection_Weapons_common": ["Reference",2, 6],
        "itemCollection_Weapons_uncommon": ["Reference",2, 6],
        "itemCollection_EquipmentRare": ["Reference",2, 4],
        "itemCollection_EquipmentUncommon": ["Reference",2, 5],
        "itemCollection_EquipmentCommon": ["Reference",2, 8],
        "itemCollection_InnerSphere_Medium_Mech_Parts": ["Reference",2, 5],
        "itemCollection_InnerSphere_Medium_Mechs": ["Reference",2, 5]
    },
    "minor_Kurita": {
                "GN_Ammo_Common": ["Reference",2, 1],
                "GN_Ammo_CommonII": ["Reference",2, 1],
                "GN_EngineCore": ["Reference",3, 1],
                "itemCollection_Weapons_common": ["Reference",4, 6],
                "itemCollection_Weapons_uncommon": ["Reference",2, 6],
                "itemCollection_EquipmentUncommon": ["Reference",1, 5],
                "itemCollection_EquipmentCommon": ["Reference",2, 8]
    },

    "faction_Ives": {},
    "Honored_Ives": {},
    "major_Ives":{
        "GN_Ammo_Common": ["Reference",2, 1],
        "GN_Ammo_CommonII": ["Reference",2, 1],
        "itemCollection_HighEndEngines": ["Reference",2, 7],
        "itemCollection_Weapons_common": ["Reference",2, 6],
        "itemCollection_Weapons_uncommon": ["Reference",2, 6],
        "itemCollection_EquipmentRare": ["Reference",2, 4],
        "itemCollection_EquipmentUncommon": ["Reference",2, 5],
        "itemCollection_EquipmentCommon": ["Reference",2, 8],
        "itemCollection_InnerSphere_Medium_Mech_Parts": ["Reference",2, 5],
        "itemCollection_InnerSphere_Medium_Mechs": ["Reference",2, 5]
    },
    "minor_Ives": {
    "GN_Ammo_Common": ["Reference",2, 1],
                "GN_Ammo_CommonII": ["Reference",2, 1],
                "GN_EngineCore": ["Reference",3, 1],
                "itemCollection_Weapons_common": ["Reference",4, 6],
                "itemCollection_Weapons_uncommon": ["Reference",2, 6],
                "itemCollection_EquipmentUncommon": ["Reference",1, 5],
                "itemCollection_EquipmentCommon": ["Reference",2, 8]
    },
 "faction_Rasalhague": {},
    "Honored_Rasalhague": {},
    "major_Rasalhague":{
        "GN_Ammo_Common": ["Reference",2, 1],
        "GN_Ammo_CommonII": ["Reference",2, 1],
        "itemCollection_HighEndEngines": ["Reference",2, 7],
        "itemCollection_Weapons_common": ["Reference",2, 6],
        "itemCollection_Weapons_uncommon": ["Reference",2, 6],
        "itemCollection_EquipmentRare": ["Reference",2, 4],
        "itemCollection_EquipmentUncommon": ["Reference",2, 5],
        "itemCollection_EquipmentCommon": ["Reference",2, 8],
        "itemCollection_InnerSphere_Medium_Mech_Parts": ["Reference",2, 5],
        "itemCollection_InnerSphere_Medium_Mechs": ["Reference",2, 5]
    },
    "minor_Rasalhague": {
     "GN_Ammo_Common": ["Reference",2, 1],
                "GN_Ammo_CommonII": ["Reference",2, 1],
                "GN_EngineCore": ["Reference",3, 1],
                "itemCollection_Weapons_common": ["Reference",4, 6],
                "itemCollection_Weapons_uncommon": ["Reference",2, 6],
                "itemCollection_EquipmentUncommon": ["Reference",1, 5],
                "itemCollection_EquipmentCommon": ["Reference",2, 8]
    },

    "faction_WordOfBlake": {},
    "Honored_WordOfBlake": {},
    "major_WordOfBlake":{
        "GN_Ammo_Common": ["Reference",2, 1],
        "GN_Ammo_CommonII": ["Reference",2, 1],
        "itemCollection_HighEndEngines": ["Reference",2, 7],
        "itemCollection_Weapons_common": ["Reference",2, 6],
        "itemCollection_Weapons_uncommon": ["Reference",2, 6],
        "itemCollection_EquipmentRare": ["Reference",2, 4],
        "itemCollection_EquipmentUncommon": ["Reference",2, 5],
        "itemCollection_EquipmentCommon": ["Reference",2, 8],
        "itemCollection_InnerSphere_Medium_Mech_Parts": ["Reference",2, 5],
        "itemCollection_InnerSphere_Medium_Mechs": ["Reference",2, 5]
    },
    "minor_WordOfBlake": {
     "GN_Ammo_Common": ["Reference",2, 1],
                "GN_Ammo_CommonII": ["Reference",2, 1],
                "GN_EngineCore": ["Reference",3, 1],
                "itemCollection_Weapons_common": ["Reference",4, 6],
                "itemCollection_Weapons_uncommon": ["Reference",2, 6],
                "itemCollection_EquipmentUncommon": ["Reference",1, 5],
                "itemCollection_EquipmentCommon": ["Reference",2, 8]
    },
                                   #-------------------------Periphery Factions--------------------
#-------------------------Periphery Factions--------------------
"faction_TaurianConcordat": {},
"Honored_TaurianConcordat": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_TaurianConcordat": {
      "itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_TaurianConcordat": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_MagistracyOfCanopus": {},
"Honored_MagistracyOfCanopus": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_MagistracyOfCanopus": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_MagistracyOfCanopus": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_AuriganDirectorate": {},
"Honored_AuriganDirectorate": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_AuriganDirectorate": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_AuriganDirectorate": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_AuriganRestoration": {},
"Honored_AuriganRestoration": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_AuriganRestoration": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_AuriganRestoration": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Axumite": {},
"Honored_Axumite": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Axumite": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Axumite": {  "GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "Periphery_Light_Mech_Parts": ["Reference",2, 8]
       },

"faction_Castile": {},
"Honored_Castile": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Castile": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Castile": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Chainelane": {},
"Honored_Chainelane": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Chainelane": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Chainelane": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Circinus": {},
"Honored_Circinus": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Circinus": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Circinus": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Delphi": {},
"Honored_Delphi": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Delphi": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Delphi": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Elysia": {},
"Honored_Elysia": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Elysia": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Elysia": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Hanse": {},
"Honored_Hanse": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Hanse": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Hanse": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Illyrian": {},
"Honored_Illyrian": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Illyrian": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Illyrian": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_JarnFolk": {},
"Honored_JarnFolk": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_JarnFolk": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_JarnFolk": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Lothian": {},
"Honored_Lothian": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Lothian": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Lothian": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Marian": {},
"Honored_Marian": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Marian": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Marian": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Oberon": {},
"Honored_Oberon": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Oberon": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Oberon": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Outworld": {},
"Honored_Outworld": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Outworld": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Outworld": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Tortuga": {},
"Honored_Tortuga": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Tortuga": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Tortuga": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Valkyrate": {},
"Honored_Valkyrate": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Valkyrate": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Valkyrate": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},
"faction_Rim": {},
"Honored_Rim": {
"itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
"itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
"itemCollection_EquipmentPeripheryRare": ["Reference",1, 8],
"GN_Ammo_Common": ["Reference",1, 1],
"item_Collection_InnerSphere_Light_Mechs": ["Reference",1, 8],
"item_Collection_InnerSphere_Medium_Mechs": ["Reference",1, 8]
},
"major_Rim": {
"itemCollection_Periphery_Light_Mechs": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mechs": ["Reference",1, 8],
      "itemCollection_Weapons_Periphery": ["Reference",3, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",2, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",1, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",1, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",1, 8],
      "GN_Ammo_Common": ["Reference",3, 1]
},
"minor_Rim": {
"GN_Ammo_Common": ["Reference",2, 1],
      "GN_Ammo_CommonII": ["Reference",2, 1],
      "GN_EngineCore": ["Reference",3, 1],
      "itemCollection_Weapons_Periphery": ["Reference",6, 6],
      "itemCollection_EquipmentPeripheryUncommon": ["Reference",1, 5],
      "itemCollection_EquipmentPeripheryCommon": ["Reference",2, 8],
      "itemCollection_Periphery_Medium_Mech_Parts": ["Reference",2, 8],
      "itemCollection_Periphery_Light_Mech_Parts": ["Reference",2, 8],
},

   "faction_ClanBurrock": {},
"Honored_ClanBurrock": {},
"major_ClanBurrock": {},
"minor_ClanBurrock": {},

"faction_ClanCloudCobra": {},
"Honored_ClanCloudCobra": {},
"major_ClanCloudCobra": {},
"minor_ClanCloudCobra": {},

"faction_ClanCoyote": {},
"Honored_ClanCoyote": {},
"major_ClanCoyote": {},
"minor_ClanCoyote": {},

"faction_ClanDiamondShark": {},
"Honored_ClanDiamondShark": {},
"major_ClanDiamondShark": {},
"minor_ClanDiamondShark": {},

"faction_ClanFireMandrill": {},
"Honored_ClanFireMandrill": {},
"major_ClanFireMandrill": {},
"minor_ClanFireMandrill": {},

"faction_ClanGhostBear": {},
"Honored_ClanGhostBear": {},
"major_ClanGhostBear": {},
"minor_ClanGhostBear": {},

"faction_ClanGoliathScorpion": {},
"Honored_ClanGoliathScorpion": {},
"major_ClanGoliathScorpion": {},
"minor_ClanGoliathScorpion": {},

"faction_ClanHellsHorses": {},
"Honored_ClanHellsHorses": {},
"major_ClanHellsHorses": {},
"minor_ClanHellsHorses": {},

"faction_ClanIceHellion": {},
"Honored_ClanIceHellion": {},
"major_ClanIceHellion": {},
"minor_ClanIceHellion": {},

"faction_ClanJadeFalcon": {},
"Honored_ClanJadeFalcon": {},
"major_ClanJadeFalcon": {},
"minor_ClanJadeFalcon": {},

"faction_ClanNovaCat": {},
"Honored_ClanNovaCat": {},
"major_ClanNovaCat": {},
"minor_ClanNovaCat": {},

"faction_ClansGeneric": {},
"Honored_ClansGeneric": {},
"major_ClansGeneric": {},
"minor_ClansGeneric": {},

"faction_ClanSmokeJaguar": {},
"Honored_ClanSmokeJaguar": {},
"major_ClanSmokeJaguar": {},
"minor_ClanSmokeJaguar": {},

"faction_ClanSnowRaven": {},
"Honored_ClanSnowRaven": {},
"major_ClanSnowRaven": {},
"minor_ClanSnowRaven": {},

"faction_ClanStarAdder": {},
"Honored_ClanStarAdder": {},
"major_ClanStarAdder": {},
"minor_ClanStarAdder": {},

"faction_ClanSteelViper": {},
"Honored_ClanSteelViper": {},
"major_ClanSteelViper": {},
"minor_ClanSteelViper": {},

"faction_ClanWolf": {},
"Honored_ClanWolf": {},
"major_ClanWolf": {},
"minor_ClanWolf": {}
}
script_dir = os.path.dirname(os.path.abspath(__file__))
new_folder = "data"
output_directory = os.path.join(script_dir, new_folder)
os.makedirs(output_directory, exist_ok=True)
for category in categories:
    # Loop through the categories
    for category, subcategories in categories.items():
        # Loop through subcategories
        for subcategory, items in subcategories.items():
            # Check if the subcategory is not empty
            if items:
                # Create a CSV file for each non-empty subcategory
                file_path = f"{output_directory}/GN_{subcategory}.csv"
                with open(file_path, 'w', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow([f"GN_{category}_{subcategory}", '', '', ''])
                    # Write the items within the current subcategory into the corresponding CSV file
                    for item, values in items.items():
                        csvwriter.writerow([item, category] + values)


# Second loop output in a subfolder inside the first loop's output directory
data_folder = os.path.join(output_directory)
os.makedirs(data_folder, exist_ok=True)

for main_category, subcategories in item_Collection.items():
    if isinstance(subcategories, dict) and len(subcategories) > 0:
        if main_category in ["Liked_InnerSphere", "Liked_Periphery", "Liked_Clans", "Honored_ComStar"]:
            file_path = f"{output_directory}\\GN_{main_category}.csv"
        else:
            file_path = f"{data_folder}\\itemCollection_{main_category}.csv"
            
        with open(file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            if main_category in ["Liked_InnerSphere", "Liked_Periphery", "Liked_Clans"]:
                csvwriter.writerow([f"GN_{main_category}", '', '', ''])
            else:
                csvwriter.writerow([f"itemCollection_{main_category}", '', '', ''])
                
            for item, values in subcategories.items():
                csvwriter.writerow([item] + values)

