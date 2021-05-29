import cpuinfo
from PyQt5.QtCore import QThread

class Loop(QThread):
    
    def size(byte):
        #Esta Função Faz a Conversão de bytes Para Um Formato Mais Legivel ao Usuario.

        for i in ["B","KB","MB","GB","TB"]:
            if byte < 1024:
                return f"{byte:.2f} {i}"
            byte = byte / 1024

    # Imprimir Informações da CPU.
    def print_CPU(self, ui):

        CPUInfo = cpuinfo.get_cpu_info()
        
        # Tenta Obter Informações Sobre o "Name", Caso Não Encontre Desligar lineEdit
        if "vendor_id_raw" in CPUInfo:
            ui.lineEdit_Name.setText(str(CPUInfo['vendor_id_raw']))
        else:
            ui.lineEdit_Name.setEnabled(False)

        # Tenta Obter Informações Sobre o "Codename", Caso Não Encontre Desligar o lineEdit
        if "CODENAME" in CPUInfo:
            ui.lineEdit_Codename.setText(str(CPUInfo['CODENAME']))
        else:
            ui.lineEdit_Codename.setEnabled(False)

        # Tenta Obter Informações Sobre o "Max TDP", Caso Não Encontre Desligar lineEdit
        if "MAX_TDP" in CPUInfo:
            ui.lineEdit_Max_TDP.setText(str(CPUInfo['MAX_TDP']))
        else:
            ui.lineEdit_Max_TDP.setEnabled(False)

        # Tenta Obter Informações Sobre o "Package Socket", Caso Não Encontre Desligar lineEdit
        if "PACKAGE_SOCKET" in CPUInfo:
            ui.lineEdit_Package_Socket.setText(str(CPUInfo['PACKAGE_SOCKET']))
        else:
            ui.lineEdit_Package_Socket.setEnabled(False)

        # Tenta Obter Informações Sobre o "Tecnology", Caso Não Encontre Desligar lineEdit
        if "TECNOLOGY" in CPUInfo:
            ui.lineEdit_Nanometer.setText(str(CPUInfo['TECNOLOGY']))
        else:
            ui.lineEdit_Nanometer.setEnabled(False)
        
        # Tenta Obter Informações Sobre o "Core Voltage", Caso Não Encontre Desligar lineEdit
        if "CORE_VOLTAGE" in CPUInfo:
            ui.lineEdit_Core_Voltage.setText(str(CPUInfo['CORE_VOLTAGE']))
        else:
            ui.lineEdit_Core_Voltage.setEnabled(False)
        
        # Tenta Obter Informações Sobre o "Ext Family", Caso Não Encontre Desligar lineEdit
        if "EXTFAMILY" in CPUInfo:
            ui.lineEdit_ExtFamily.setText(str(CPUInfo['EXTFAMILY']))
        else:
            ui.lineEdit_ExtFamily.setEnabled(False)
        
        # Tenta Obter Informações Sobre o "Ext Model", Caso Não Encontre Desligar lineEdit
        if "EXTMODEL" in CPUInfo:
            ui.lineEdit_ExtModel.setText(str(CPUInfo['EXTMODEL']))
        else:
            ui.lineEdit_ExtModel.setEnabled(False)

        # Tenta Obter Informações Sobre o "Revision", Caso Não Encontre Desligar lineEdit
        if "REVISION" in CPUInfo:
            ui.lineEdit_Revision.setText(str(CPUInfo['REVISION']))
        else:
            ui.lineEdit_Revision.setEnabled(False)

        # Tenta Obter Informações Sobre o "Multiplier", Caso Não Encontre Desligar lineEdit
        if "MULTIPLIER" in CPUInfo:
            ui.lineEdit_Multiplier.setText(str(CPUInfo['MULTIPLIER']))
        else:
            ui.lineEdit_Multiplier.setEnabled(False)

        # Tenta Obter Informações Sobre o "BUSSpeed", Caso Não Encontre Desligar lineEdit
        if "BUSSpeed" in CPUInfo:
            ui.lineEdit_BUSSpeed.setText(str(CPUInfo['BUSSpeed']))
        else:
            ui.lineEdit_BUSSpeed.setEnabled(False)

        # Tenta Obter Informações Sobre o "RatedFSB", Caso Não Encontre Desligar lineEdit
        if "RatedFSB" in CPUInfo:
            ui.lineEdit_RatedFSB.setText(str(CPUInfo['RatedFSB']))
        else:
            ui.lineEdit_RatedFSB.setEnabled(False)

        # Tenta Obter Informações Sobre o "HARDWARE_RAW", Caso Não Encontre Desligar o lineEdit
        if "hardware_raw" in CPUInfo:
            ui.lineEdit_Package_Socket.setText(str(CPUInfo['hardware_raw']))
        else:
            ui.lineEdit_Package_Socket.setEnabled(False)

        # Tenta Obter Informações Sobre o "SPECIFICATION", Caso Não Encontre Desligar lineEdit
        if "brand_raw" in CPUInfo:
            ui.lineEdit_Specification.setText(str(CPUInfo['brand_raw']))
        else:
            ui.lineEdit_Specification.setEnabled(False)

        # Tenta Obter Informações Sobre o "FAMILY", Caso Não Encontre Desligar lineEdit
        if "family" in CPUInfo:
            ui.lineEdit_Family.setText(str(CPUInfo['family']))
        else:
            ui.lineEdit_Family.setEnabled(False)

        # Tenta Obter Informações Sobre o "MODEL", Caso Não Encontre Desligar lineEdit
        if "model" in CPUInfo:
            ui.lineEdit_Model.setText(str(CPUInfo['model']))
        else:
            ui.lineEdit_Model.setEnabled(False)

        # Tenta Obter Informações Sobre o STEPPING, Caso Não Encontre Desligar lineEdit
        if "stepping" in CPUInfo:
            ui.lineEdit_Stepping.setText(str(CPUInfo['stepping']))
        else:
            ui.lineEdit_Stepping.setEnabled(False)

        # Tenta Obter Informações Sobre o FLAGS, Caso Não Encontre Desligar lineEdit
        if "flags" in CPUInfo:
            ui.textEdit.setText(str(CPUInfo['flags']).upper())
        else:
            ui.textEdit.setEnabled(False)

        # Tenta Obter Informações Sobre o FREQUENCIA, Caso Não Encontre Desligar lineEdit
        if "hz_actual_friendly" in CPUInfo:
            ui.lineEdit_CoreSpeed.setText(str(CPUInfo['hz_actual_friendly']))
        else:
            ui.lineEdit_CoreSpeed.setEnabled(False)


    def print_Cache(self, ui):

        CPUInfo = cpuinfo.get_cpu_info()

        # Tenta Obter Informações Sobre "Cache L1", Caso Não Encontre Desligar lineEdit
        if "l1_data_cache_size" in CPUInfo:
            ui.lineEdit_L1Data.setText(str(Loop.size(CPUInfo['l1_data_cache_size'])))
        else:
            ui.lineEdit_L1Data.setEnabled(False)

        # Tenta Obter Informações Sobre "Cache Size", Caso Não Encontre Desligar lineEdit
        if "l1_instruction_cache_size" in CPUInfo:
            ui.lineEdit_L1Inst.setText(str(Loop.size(CPUInfo['l1_instruction_cache_size'])))
        else:
            ui.lineEdit_L1Inst.setEnabled(False)

        # Tenta Obter Informações Sobre "Cache L2", Caso Não Encontre Desligar lineEdit
        if "l2_cache_size" in CPUInfo:
            ui.lineEdit_L2.setText(str(Loop.size(CPUInfo['l2_cache_size'])))
        else:
            ui.lineEdit_L2.setEnabled(False)

        # Tenta Obter Informações Sobre "Cache L3", Caso Não Encontre Desligar lineEdit
        if "l3_cache_size" in CPUInfo:
            ui.lineEdit_L3.setText(str(Loop.size(CPUInfo['l3_cache_size'])))
        else:
            ui.lineEdit_L3.setEnabled(False)

