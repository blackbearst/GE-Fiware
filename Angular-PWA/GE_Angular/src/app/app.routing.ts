// import modules of router angular
import {ModuleWithProviders} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';

//import components
import {GeReportGComponent} from './components/ge-report-g/ge-report-g.component';
import {GeReportComponent} from './components/ge-report/ge-report.component';
import {HomeComponent} from './components/home/home.component';
import {HelpComponent} from './components/help/help.component';

//array of rutes
const appRoutes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'report_g', component: GeReportGComponent},
    {path: 'kurento',component: GeReportComponent},
    {path: 'help', component: HelpComponent},
    {path: '**', component: HomeComponent}
];

//export module of router
export const appRoutingProviders: any[] = [];
export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);