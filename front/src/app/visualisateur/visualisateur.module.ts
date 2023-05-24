import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';

import {VisualisateurComponent} from './visualisateur.component';
import {DragAndDropModule} from '../drag-and-drop/drag-and-drop.module';

@NgModule({
  declarations: [VisualisateurComponent],
  imports: [CommonModule, DragAndDropModule],
  exports: [VisualisateurComponent]
})
export class VisualisateurModule {
}
