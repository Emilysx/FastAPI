// // Função assíncrona para puxar dados da API
// async function puxando_api() {
//     // Faz a requisição GET para a API
//     const response = await fetch("http://localhost:8000/api/v1/bandas/");

//     // Retorna os dados da resposta em formato JSON
//     const data = await response.json();
//     return data; // Retorna os dados que serão usados no frontend
    
// }

// // Função assíncrona para mostrar as bandas no HTML
// async function mostrar_banda() {
//     const bandas = await puxando_api();
//     const container = document.getElementById("bandas-conteiner"); // Seleciona o container para inserir as bandas

//     // Loop para cada banda, cria o HTML e insere no container
//     bandas.forEach(banda => {
//         // Cria uma div para cada banda
//         const bandaDiv = document.createElement('div');
//         bandaDiv.classList.add('banda');

//         // Preenche a div com informações sobre a banda
//         bandaDiv.innerHTML = `
//         <h2> ${banda.nome}</h2>
//         <p>${banda.qtd_integrantes}</p>
//         <p>${banda.tipo_musical}</p>
//         `;
//         container.appendChild(bandaDiv);
 
//     });   
// }

// mostrar_banda()


// Função assíncrona para puxar dados da API usando Axios
async function puxar_api() {
    // Faz a requisição GET para a API
    await axios.get("http://localhost:8000/api/v1/bandas/").then((response) =>{
        const bandas = response.data;
        const container = document.getElementById("bandas-conteiner");

        // Loop para cada banda e cria um novo elemento no HTML
        bandas.forEach(element => {
            const bandaDiv = document.createElement('div');
            bandaDiv.classList.add('banda');

            // Preenche a div com as informações da banda
            bandaDiv.innerHTML= `
            <h2>${element.nome}</h2>
            <p>${element.qtd_integrantes}</p>
            <p>${element.tipo_musical}</p>
            `
            container.append(bandaDiv);
        });
    });
    
}

puxar_api()