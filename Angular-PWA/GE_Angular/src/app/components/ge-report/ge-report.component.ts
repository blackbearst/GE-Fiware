import { Component, OnInit } from '@angular/core';
import {GeReportService} from '../../services/ge-report.service';
import {GeReport} from '../../gereport';

@Component({
  selector: 'ge-report',
  templateUrl: './ge-report.component.html',
  styleUrls: ['./ge-report.component.css']
})
export class GeReportComponent implements OnInit {
  geReports: GeReport[];

  constructor(private gereportService: GeReportService) {
    this.gereportService.getGEreport()
    .subscribe(geReports => {
      console.log(geReports);
      this.geReports = geReports
    })
   }

  ngOnInit() {
  }

}
