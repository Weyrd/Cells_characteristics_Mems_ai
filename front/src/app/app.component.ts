import {Component} from '@angular/core';
import * as d3 from 'd3';
import {VisualisateurComponent} from "./visualisateur/visualisateur.component";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'Mems IA';


  resetSite(): void {
    VisualisateurComponent.prototype.resetImages();
  }
}

