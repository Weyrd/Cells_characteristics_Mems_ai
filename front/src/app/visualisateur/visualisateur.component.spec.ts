import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisualisateurComponent } from './visualisateur.component';

describe('VisualisateurComponent', () => {
  let component: VisualisateurComponent;
  let fixture: ComponentFixture<VisualisateurComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [VisualisateurComponent]
    });
    fixture = TestBed.createComponent(VisualisateurComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
