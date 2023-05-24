import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {VisualisateurModule} from './visualisateur/visualisateur.module';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    VisualisateurModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
