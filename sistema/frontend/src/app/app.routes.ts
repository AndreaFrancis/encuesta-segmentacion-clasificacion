import {Routes} from "@angular/router";
import {HomeComponent} from "./pages/home/home.component";

export const ROUTES: Routes = [
    // routes from pages
    {path: 'home', component: HomeComponent, data: {title: 'Encuesta TICs'}},

    // default redirect
    {path: '**', redirectTo: '/home'}
];