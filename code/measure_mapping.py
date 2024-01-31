"""
Based on the table https://github.com/buildingSMART/IDS/blob/master/Documentation/units.md

Numerical values of physical quantities are represented using SI units. The following table lists the physical quantities and their units. 
A full list of IFC Defined types can be found in the IFC documentation. For example for IFC 4ADD2TC1 it is here: https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD2_TC1/HTML/link/alphabeticalorder-defined-types.htm
"""

MEASURE_MAPPING = {
    # Ifc Defined Type name --> Dimensional exponents
    'IfcAreaDensityMeasure': '-2 1 0 0 0 0 0',
    'IfcAreaMeasure': '2 0 0 0 0 0 0',
    'IfcDynamicViscosityMeasure': '-1 1 -1 0 0 0 0',
    'IfcElectricCapacitanceMeasure': '-2 1 4 1 0 0 0',
    'IfcElectricChargeMeasure': '0 0 1 1 0 0 0',
    'IfcElectricConductanceMeasure': '-2 -1 3 2 0 0 0',
    'IfcElectricCurrentMeasure': '0 0 0 1 0 0 0',
    'IfcElectricResistanceMeasure': '2 1 -3 -2 0 0 0',
    'IfcElectricVoltageMeasure': '2 1 -3 -1 0 0 0',
    'IfcEnergyMeasure': '2 1 -2 0 0 0 0',
    'IfcForceMeasure': '1 1 -2 0 0 0 0',
    'IfcFrequencyMeasure': '0 0 -1 0 0 0 0',
    'IfcHeatFluxDensityMeasure': '0 1 -3 0 0 0 0',
    'IfcHeatingValueMeasure': '2 1 -2 0 -1 0 0',
    'IfcIlluminanceMeasure': '-2 0 0 0 0 0 1',
    'IfcIonConcentrationMeasure': '-3 1 0 0 0 0 0',
    'IfcIsothermalMoistureCapacityMeasure': '3 -1 0 0 0 0 0',
    'IfcLengthMeasure': '1 0 0 0 0 0 0',
    'IfcLinearVelocityMeasure': '1 0 -1 0 0 0 0',
    'IfcLuminousFluxMeasure': '0 0 0 0 0 0 1',
    'IfcLuminousIntensityMeasure': '0 0 0 0 0 0 1',
    'IfcMassDensityMeasure': '-3 1 0 0 0 0 0',
    'IfcMassFlowRateMeasure': '0 1 -1 0 0 0 0',
    'IfcMassMeasure': '0 1 0 0 0 0 0',
    'IfcMassPerLengthMeasure': '-1 1 0 0 0 0 0',
    'IfcModulusOfElasticityMeasure': '-1 1 -2 0 0 0 0',
    'IfcMoistureDiffusivityMeasure': '3 0 -1 0 0 0 0',
    'IfcMolecularWeightMeasure': '0 1 0 0 0 -1 0',
    'IfcMomentOfInertiaMeasure': '4 0 0 0 0 0 0',
    'IfcPHMeasure': '0 0 0 0 0 0 0',
    'IfcPlanarForceMeasure': '-1 1 -2 0 0 0 0',
    'IfcPlaneAngleMeasure': '0 0 0 0 0 0 0',
    'IfcPressureMeasure': '-1 1 -2 0 0 0 0',
    'IfcRadioActivityMeasure': '0 0 -1 0 0 0 0',
    'IfcRatioMeasure': '0 0 0 0 0 0 0',
    'IfcRotationalFrequencyMeasure': '0 0 -1 0 0 0 0',
    'IfcSectionModulusMeasure': '3 0 0 0 0 0 0',
    'IfcSoundPowerMeasure': '0 0 0 0 0 0 0',
    'IfcSoundPressureMeasure': '0 0 0 0 0 0 0',
    'IfcSpecificHeatCapacityMeasure': '2 0 -2 0 -1 0 0',
    'IfcTemperatureRateOfChangeMeasure': '0 0 -1 0 1 0 0',
    'IfcThermalConductivityMeasure': '1 1 -3 0 -1 0 0',
    'IfcThermodynamicTemperatureMeasure': '0 0 0 0 1 0 0',
    'IfcTimeMeasure': '0 0 1 0 0 0 0',
    'IfcTorqueMeasure': '2 1 -2 0 0 0 0',
    'IfcVaporPermeabilityMeasure': '0 0 1 0 0 0 0',
    'IfcVolumeMeasure': '3 0 0 0 0 0 0',
    'IfcVolumetricFlowRateMeasure': '3 0 -1 0 0 0 0'
 }
