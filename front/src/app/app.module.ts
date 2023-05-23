import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DragAndDropModule } from './drag-and-drop/drag-and-drop.module';
import { VisualisateurComponent } from './visualisateur/visualisateur.component';

@NgModule({
  declarations: [
    AppComponent,
    VisualisateurComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    DragAndDropModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
