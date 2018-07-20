import { TestBed, inject } from '@angular/core/testing';

import { GeReportService } from './ge-report.service';

describe('GeReportService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GeReportService]
    });
  });

  it('should be created', inject([GeReportService], (service: GeReportService) => {
    expect(service).toBeTruthy();
  }));
});
