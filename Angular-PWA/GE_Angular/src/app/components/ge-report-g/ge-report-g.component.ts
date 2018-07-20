import { Component, OnInit } from '@angular/core';
import {GeReportService} from '../../services/ge-report.service';
import {GeReport} from '../../gereport';

@Component({
  selector: 'app-ge-report-g',
  templateUrl: './ge-report-g.component.html',
  styleUrls: ['./ge-report-g.component.css']
})
export class GeReportGComponent implements OnInit {

  geReports: GeReport[];

  constructor(private gereportService: GeReportService) {
    this.gereportService.getGErep()
    .subscribe(geReports => {
      console.log(geReports);
      this.geReports = geReports
    })
   }

  ngOnInit() {
  }

}
