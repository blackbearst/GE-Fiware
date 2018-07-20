import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GeReportGComponent } from './ge-report-g.component';

describe('GeReportGComponent', () => {
  let component: GeReportGComponent;
  let fixture: ComponentFixture<GeReportGComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GeReportGComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GeReportGComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
