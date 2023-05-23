import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-visualisateur',
  templateUrl: './visualisateur.component.html',
  styleUrls: ['./visualisateur.component.css']
})
export class VisualisateurComponent {
  @Input() message: string | undefined;
}
