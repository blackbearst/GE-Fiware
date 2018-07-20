import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import {routing, appRoutingProviders} from './app.routing'

import {GeReportService} from'./services/ge-report.service'; //import GeReport service 

import { AppComponent } from './app.component';
import { EjemploComponent } from './components/ejemplo/ejemplo.component';
import { MenuComponent } from './components/menu/menu.component';
import { OrionComponent } from './components/orion/orion.component';
import { WirecloudComponent } from './components/wirecloud/wirecloud.component';
import { KnowageComponent } from './components/knowage/knowage.component';
import { WilmaComponent } from './components/wilma/wilma.component';
import { KeyrockComponent } from './components/keyrock/keyrock.component';
import { AuthzforceComponent } from './components/authzforce/authzforce.component';
import { AeonComponent } from './components/aeon/aeon.component';
import { BotonComponent } from './components/boton/boton.component';
import { CheckboxComponent } from './components/checkbox/checkbox.component';
import { Boton2Component } from './components/boton2/boton2.component';
import { GeReportComponent } from './components/ge-report/ge-report.component';
import { HttpClientModule } from '@angular/common/http';
import { HomeComponent } from './components/home/home.component';
import { GeReportGComponent } from './components/ge-report-g/ge-report-g.component';
import { HelpComponent } from './components/help/help.component';

@NgModule({
  declarations: [
    AppComponent,
    EjemploComponent,
    MenuComponent,
    OrionComponent,
    WirecloudComponent,
    KnowageComponent,
    WilmaComponent,
    KeyrockComponent,
    AuthzforceComponent,
    AeonComponent,
    BotonComponent,
    CheckboxComponent,
    Boton2Component,
    GeReportComponent,
    HomeComponent,
    GeReportGComponent,
    HelpComponent,
   
  ], 
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    routing
  ],
  providers: [
    GeReportService,
    appRoutingProviders 
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
