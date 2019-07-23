export class Sintoma {
    // vcm: number = 0;
    // hbcm: number = 0;
    // chbcm: number = 0;
    // glucosa: number = 0;
    // creatinina: number = 0;
    // sodio: number = 0;
    // potasio: number = 0;
    // cloro: number = 0;
    // globulosBlancos: number = 0;
    // globulosRojos: number = 0;
    // plaquetas: number = 0;
    // neutrofilos: number = 0;
    // linfocitos: number = 0;
    // monocitos: number = 0;
    // edad: number = 0;
    // sexo: string = 'F';

    // sepalLength: number = 5.0;
    // sepalWidth: number = 3.5;
    // petalLength: number = 2.5;
    // petalWidth: number = 1.2;
    name: string;
    value: boolean;

    constructor(name, value){
        this.name = name;
        this.value = value;
    }
}

export class ProbabilityPrediction {
    name: string;
    value: number;
}

export class SVCParameters {
    C: number = 2.0;
}

export class SVCResult {
    accuracy: number;
}
