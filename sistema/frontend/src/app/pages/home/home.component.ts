import {Component, OnInit } from '@angular/core';
import {IrisService} from "./iris.service";
import {
    Sintoma,
    ProbabilityPrediction,
    SVCParameters,
    SVCResult
} from "./types";

@Component({
    selector: 'home',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.scss']
})
export class HomeComponent //implements OnInit
 {

    public svcParameters: SVCParameters = new SVCParameters();
    public svcResult: SVCResult;
    public sintomas1: Sintoma[];
    public sintomas2: Sintoma[];
    public sintomas3: Sintoma[];
    public sintomas4: Sintoma[];
    public probabilityPredictions: ProbabilityPrediction[];
    public disableTooltip = false;
    public showResult = false;
    public showForm = false;

    // graph styling
    public colorScheme = {
        domain: ['#7D3C98', '#5499C7', '#5DADE2', '#48C9B0', '#45B39D', '#73C6B6', '#F4D03F', '#EB984E',
    '#EB984E', '#D35400', '#95A5A6', '#34495E', '#17202A']
    };

    constructor(private irisService: IrisService) {
        this.fillSimptoms();
        this.disableTooltip = false;
        this.showResult = false;
        this.showForm = false;
    }

    // ngOnInit() {
    //     this.fillSimptoms();
    //     this.disableTooltip = false;
    //     this.showResult = false;
    //     this.showForm = false;
    // }

    public trainModel() {
        this.irisService.trainModel(this.svcParameters).subscribe((svcResult) => {
            this.svcResult = svcResult;
        });
    }

    public fillSimptoms(){
        this.sintomas1 = [];
        this.sintomas2 = [];
        this.sintomas3 = [];
        this.sintomas4 = [];
        this.sintomas1.push(new Sintoma("Abdominal", false));
        this.sintomas1.push(new Sintoma("Acidez", false));
        this.sintomas1.push(new Sintoma("Alcalina", false));
        this.sintomas1.push(new Sintoma("Alcohol", false));
        this.sintomas1.push(new Sintoma("Alimentacion", false));
        this.sintomas1.push(new Sintoma("Amarillo", false));
        this.sintomas1.push(new Sintoma("Amebas", false));
        this.sintomas1.push(new Sintoma("Analgesico", false));
        this.sintomas1.push(new Sintoma("Anorexia", false));
        this.sintomas1.push(new Sintoma("Ardor", false));
        this.sintomas1.push(new Sintoma("Bilis", false));
        this.sintomas1.push(new Sintoma("Chagas", false));
        this.sintomas1.push(new Sintoma("Cirrosis", false));
        this.sintomas1.push(new Sintoma("Dolor", false));
        this.sintomas1.push(new Sintoma("Enema", false));
        this.sintomas1.push(new Sintoma("Esofago", false));
        this.sintomas1.push(new Sintoma("Erge", false));
        this.sintomas1.push(new Sintoma("Erosivo", false));
        this.sintomas1.push(new Sintoma("Escalofrios", false));
        this.sintomas2.push(new Sintoma("Escozor", false));
        this.sintomas2.push(new Sintoma("Espasmodico", false));
        this.sintomas2.push(new Sintoma("Estornudo", false));
        this.sintomas2.push(new Sintoma("Estres", false));
        this.sintomas2.push(new Sintoma("Evacua", false));
        this.sintomas2.push(new Sintoma("Faringe", false));
        this.sintomas2.push(new Sintoma("Fecal", false));
        this.sintomas2.push(new Sintoma("Fiebre", false));
        this.sintomas2.push(new Sintoma("Flatulencia", false));
        this.sintomas2.push(new Sintoma("Flema", false));
        this.sintomas2.push(new Sintoma("Fumar", false));
        this.sintomas2.push(new Sintoma("Gases", false));
        this.sintomas2.push(new Sintoma("Giardias", false));
        this.sintomas2.push(new Sintoma("Gota", false));
        this.sintomas2.push(new Sintoma("Grano", false));
        this.sintomas2.push(new Sintoma("Grasas", false));
        this.sintomas2.push(new Sintoma("Hemorragia", false));
        this.sintomas2.push(new Sintoma("Hemorroides", false));
        this.sintomas2.push(new Sintoma("Hernia", false));
        this.sintomas2.push(new Sintoma("Herpes", false));
        this.sintomas3.push(new Sintoma("Ictericia", false));
        this.sintomas3.push(new Sintoma("Infeccion", false));
        this.sintomas3.push(new Sintoma("Inflamacion", false));
        this.sintomas3.push(new Sintoma("Maligno", false));
        this.sintomas3.push(new Sintoma("Mareos", false));
        this.sintomas3.push(new Sintoma("Menopausia", false));
        this.sintomas3.push(new Sintoma("Menstrual", false));
        this.sintomas3.push(new Sintoma("Mental", false));
        this.sintomas3.push(new Sintoma("Nauseas", false));
        this.sintomas3.push(new Sintoma("Neoplasia", false));
        this.sintomas3.push(new Sintoma("Neumologia", false));
        this.sintomas3.push(new Sintoma("Neumonia", false));
        this.sintomas3.push(new Sintoma("Neurologia", false));
        this.sintomas3.push(new Sintoma("Obesidad", false));
        this.sintomas3.push(new Sintoma("Omeprazol", false));
        this.sintomas3.push(new Sintoma("Oscurecimiento", false));
        this.sintomas3.push(new Sintoma("Ovarios", false));
        this.sintomas3.push(new Sintoma("Ovulos", false));
        this.sintomas3.push(new Sintoma("Palido", false));
        this.sintomas4.push(new Sintoma("Pancreatitis", false));
        this.sintomas4.push(new Sintoma("Pesades", false));
        this.sintomas4.push(new Sintoma("Helicobacter pilori", false));
        this.sintomas4.push(new Sintoma("Pirosis", false));
        this.sintomas4.push(new Sintoma("Psiquiatrico", false));
        this.sintomas4.push(new Sintoma("Psoriasis", false));
        this.sintomas4.push(new Sintoma("Quistes", false));
        this.sintomas4.push(new Sintoma("Rectorragia", false));
        this.sintomas4.push(new Sintoma("Resfrio", false));
        this.sintomas4.push(new Sintoma("Ronquera", false));
        this.sintomas4.push(new Sintoma("Sangrado", false));
        this.sintomas4.push(new Sintoma("Sudor", false));
        this.sintomas4.push(new Sintoma("Tifoidea", false));
        this.sintomas4.push(new Sintoma("Tiroides", false));
        this.sintomas4.push(new Sintoma("Trombosis", false));
        this.sintomas4.push(new Sintoma("Tumor", false));
        this.sintomas4.push(new Sintoma("Ulceras", false));
        this.sintomas4.push(new Sintoma("Vesicula", false));
        this.sintomas4.push(new Sintoma("Alergia", false));
        this.showForm = true;
        this.showResult = false;
    }

    public predictIris() {
        this.disableTooltip = true;

        let values = [];
 
        this.sintomas1.forEach(function (sintoma) { 
            values.push(sintoma.value? 1: 0);     
        });

        this.sintomas2.forEach(function (sintoma) { 
            values.push(sintoma.value? 1: 0);     
        });

        this.sintomas3.forEach(function (sintoma) { 
            values.push(sintoma.value? 1: 0);     
        });

        this.sintomas4.forEach(function (sintoma) { 
            values.push(sintoma.value? 1: 0);     
        });

        this.irisService.predictIris(values).subscribe((probabilityPredictions) => {
            this.probabilityPredictions = probabilityPredictions;
            this.disableTooltip = false;
        });
        
        this.showForm = false;
        this.showResult = true;
    }

}
