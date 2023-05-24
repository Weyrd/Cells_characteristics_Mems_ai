import {Component, Input} from '@angular/core';

@Component({
  selector: 'app-visualisateur',
  templateUrl: './visualisateur.component.html',
  styleUrls: ['./visualisateur.component.css']
})
export class VisualisateurComponent {
  private imagesUploaded: any[] = [];

  @Input()
  addImage(image: any): void {
    this.imagesUploaded.push(image);
  }

  // get length() return true or false if more than 1
  getLentListImages(): number {
    let isImage = 0
    if (this.imagesUploaded.length > 1) {
      isImage = 1;
    }
    isImage = 0;
    console.log("Il y a :", isImage);
    return isImage;
  }

  resetImages(): void {
    this.imagesUploaded = [];
  }


}
