import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GeReportComponent } from './ge-report.component';

describe('GeReportComponent', () => {
  let component: GeReportComponent;
  let fixture: ComponentFixture<GeReportComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GeReportComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GeReportComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
