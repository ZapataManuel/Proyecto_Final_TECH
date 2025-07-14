// grafica 1 solar
fetch("./datas/top15_solar.json")
      .then(res => res.json())
      .then(data => {
        const labels = Object.keys(data);
        const values = Object.values(data);

        new Chart(document.getElementById("graficoTop15"), {
          type: 'bar',
          data: {
            labels: labels,
            datasets: [{
              label: "% Energía solar (último año)",
              data: values,
              backgroundColor: "rgba(54, 162, 235, 0.6)"
            }]
          },
          options: {
            indexAxis: 'y',
            plugins: {
              title: {
                display: true,
                text: "Top 15 países europeos con mayor % de energía solar"
              }
            },
            responsive: true
          }
        });
      });

// grafica 2 solar 
fetch("./datas/promedio_solar.json")
      .then(res => res.json())
      .then(data => {
        const labels = Object.keys(data);
        const values = Object.values(data);

        new Chart(document.getElementById("graficoPromedio"), {
          type: 'bar',
          data: {
            labels: labels,
            datasets: [{
              label: "% Promedio histórico",
              data: values,
              backgroundColor: "rgba(75, 192, 192, 0.6)"
            }]
          },
          options: {
            indexAxis: 'y',
            plugins: {
              title: {
                display: true,
                text: "Promedio histórico del % de energía solar"
              }
            },
            responsive: true
          }
        });
      });


// grafica 3 continental

fetch("./datas/europa_linea.json")
  .then(res => res.json())
  .then(data => {
    const years = Object.keys(data);
    const values = Object.values(data);

    new Chart(document.getElementById("graficoEuropaLinea"), {
      type: "line",
      data: {
        labels: years,
        datasets: [{
          label: "Consumo energético Europa",
          data: values,
          borderColor: "green",
          backgroundColor: "rgba(0,128,0,0.2)",
          fill: true,
          tension: 0.3,
          pointStyle: "circle",
          pointRadius: 4
        }]
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: "Evolución del consumo energético en Europa"
          }
        },
        scales: {
          x: { title: { display: true, text: "Año" }},
          y: { title: { display: true, text: "TWh o %" }}
        }
      }
    });
  });

// grafica 4 continental

fetch("./datas/europa_barras.json")
  .then(res => res.json())
  .then(data => {
    const years = Object.keys(data);
    const values = Object.values(data);

    new Chart(document.getElementById("graficoEuropaBarras"), {
      type: "bar",
      data: {
        labels: years,
        datasets: [{
          label: "Consumo energético Europa (2000+)",
          data: values,
          backgroundColor: "seagreen"
        }]
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: "Consumo energético de Europa desde el 2000"
          }
        },
        scales: {
          x: { title: { display: true, text: "Año" }},
          y: { title: { display: true, text: "TWh o %" }}
        }
      }
    });
  });

// grafica 5 eolica 
fetch("./datas/europa_eolica.json")
    .then(res => res.json())
    .then(data => {
      const labels = Object.keys(data);
      const values = Object.values(data);

      new Chart(document.getElementById("graficoEolica"), {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: "Total generado (TWh)",
            data: values,
            backgroundColor: values.map(v => `rgba(54, 162, 235, ${0.3 + v / Math.max(...values) * 0.7})`) // tonalidad azul
          }]
        },
        options: {
          indexAxis: 'y', // barras horizontales
          responsive: true,
          plugins: {
            title: {
              display: true,
              text: "Top 10 países europeos en generación eólica (2000 en adelante)",
              font: {
                size: 18
              }
            },
            legend: {
              display: false
            }
          },
          scales: {
            x: {
              title: {
                display: true,
                text: "Total generado (TWh)"
              }
            },
            y: {
              title: {
                display: true,
                text: "País"
              }
            }
          }
        }
      });
    })

// grafica 6 eolicas

fetch("./datas/europa_eolica.json")
      .then(res => res.json())
      .then(data => {
        const countries = Object.keys(data);
        const years = Object.keys(data[countries[0]]); // se asume que todos los países tienen los mismos años

        // Construimos los datasets para Chart.js
        const datasets = countries.map((pais, i) => ({
          label: pais,
          data: years.map(year => data[pais][year]),
          fill: true,
          borderColor: `hsl(${(i * 360 / countries.length)}, 70%, 50%)`,
          backgroundColor: `hsla(${(i * 360 / countries.length)}, 70%, 50%, 0.4)`,
          tension: 0.3,
          borderWidth: 1
        }));

        new Chart(document.getElementById("graficoAreaEolica"), {
          type: 'line',
          data: {
            labels: years,
            datasets: datasets
          },
          options: {
            responsive: true,
            interaction: {
              mode: 'index',
              intersect: false
            },
            stacked: true, // área apilada
            plugins: {
              title: {
                display: true,
                text: 'Generación total de electricidad eólica en Europa por país (TWh)'
              },
              legend: {
                position: 'right'
              }
            },
            scales: {
              x: {
                title: {
                  display: true,
                  text: 'Año'
                }
              },
              y: {
                title: {
                  display: true,
                  text: 'TWh'
                }
              }
            }
          }
        });
      })

// grafica 7 hidroeléctrica
fetch("./datas/hydro_europa.json")
  .then(res => res.json())
  .then(data => {
    const labels = Object.keys(data);
    const values = Object.values(data);

    new Chart(document.getElementById("graficoHydro"), {
      type: 'pie', // ← CAMBIO AQUÍ
      data: {
        labels: labels,
        datasets: [{
          label: "% Energía hidroeléctrica (último año)",
          data: values,
          
          
        }]
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: "Distribución % de energía hidroeléctrica por país (Europa)"
          },
          legend: {
            position: 'right'
          }
          
        },
        responsive: true
      }
    });
  });

