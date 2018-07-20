import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import 'rxjs/Rx';

import {GeReport} from '../gereport';

@Injectable()
export class GeReportService {

  constructor(private http: HttpClient) {}
  domain: string='http://localhost:3000';

  getGEreport(){
    return this.http.get<GeReport[]>(`${this.domain}/api/fiware/kurento`)
    .map(res => res);
  }

  getGErep(){
    return this.http.get<GeReport[]>(`${this.domain}/api/fiware`)
    .map(res => res);
  }
}
