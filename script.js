
function handleFolderSelection(event) {
  const subfolderListContainer = document.getElementById('subfolderList');
  const fileListContainer = document.getElementById('fileList');
  subfolderListContainer.innerHTML = '';
  fileListContainer.innerHTML = '';

  const files = event.target.files;

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    if (file.isDirectory) {
      const subfolderCheckbox = createCheckbox(file.name, 'selectedSubfolders');
      subfolderListContainer.appendChild(subfolderCheckbox);
    } else {
      const fileCheckbox = createCheckbox(file.name, 'selectedFiles');
      fileListContainer.appendChild(fileCheckbox);
    }
  }
}

function createCheckbox(name, groupName) {
  const label = document.createElement('label');
  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.name = groupName;
  checkbox.value = name;
  label.appendChild(checkbox);
  label.appendChild(document.createTextNode(name));
  return label;
}

const folderInput = document.getElementById('folderInput');
folderInput.addEventListener('change', handleFolderSelection);