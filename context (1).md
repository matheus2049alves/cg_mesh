# Contexto do Projeto

## Objetivo

Rodar inferência do **MeshAnything V2** com imagens próprias, comparar os resultados contra baselines usando as métricas do paper original, e gerar tabelas e visualizações comparativas.

---

## Pipeline

```
Imagens próprias
      ↓
TripoSR → Mesh densa (ground truth)
      ↓
mesh_to_pc.py → Point Cloud
      ↓
┌─────────────────────────────────────────┐
│  MeshAnything V2 (AMT)      → Mesh      │
│  Baseline naive (sem AMT)   → Mesh      │
└─────────────────────────────────────────┘
      ↓
Avaliação: CD, ECD, NC, #V, #F, V_Ratio, F_Ratio
(100K points amostrados de cada mesh)
      ↓
Tabelas + Visualizações
```

---

## Modelos

| Modelo | Papel | Repositório |
|--------|-------|-------------|
| **TripoSR** | Gerar mesh densa a partir de imagem (ground truth + point cloud) | https://github.com/VAST-AI-Research/TripoSR |
| **MeshAnything V2** | Modelo principal avaliado | https://github.com/buaacyw/MeshAnythingV2 |
| **MeshAnything V1** (Baseline naive) | Tokenização naive sem AMT — baseline interno do paper | https://github.com/buaacyw/MeshAnything |

Todos usados **apenas em inferência**. Sem treinamento, sem fine-tuning.

### Notas sobre GPU
- MeshAnything V2 é baseado em OPT-350M (~350M parâmetros) — inferência usa ~2-4GB de VRAM
- TripoSR usa ~4-6GB de VRAM
- Ambos rodam confortavelmente na L4 (22.5GB) do Colab Pro
- Rodam em notebooks separados — sem conflito de memória

---

## Baselines

| Baseline | Descrição |
|----------|-----------|
| **Baseline naive** | Tokenização naive onde cada face usa 3 vértices — método dos trabalhos anteriores |

> O paper também testa **PolyGen (AMT)**, **Unsort** e **AMT(Swap)** — PolyGen descartado deste benchmark.

---

## Métricas

Calculadas amostrando **100K points** de cada mesh (conforme ablation principal do paper):

| Métrica | Descrição | Direção |
|---------|-----------|---------|
| **CD** — Chamfer Distance (×10⁻²) | Qualidade geral da mesh | ↓ |
| **ECD** — Edge Chamfer Distance (×10⁻²) | Preservação de bordas e cantos | ↓ |
| **NC** — Normal Consistency | Qualidade das normais de superfície | ↑ |
| **#V** | Número de vértices | ↓ |
| **#F** | Número de faces | ↓ |
| **V_Ratio** | Razão vértices gerados / ground truth | ↓ |
| **F_Ratio** | Razão faces geradas / ground truth | ↓ |

> **S_Ratio fora do escopo:** métrica interna de compressão de tokenização, não avalia qualidade geométrica da mesh.

---

## Infraestrutura

| Ambiente | Uso |
|----------|-----|
| **Google Colab Pro** | Toda tarefa com GPU — inferência dos modelos, cálculo de métricas |
| **VS Code + GitHub** | Desenvolvimento e versionamento |
| **Python 3.10+** | Linguagem principal |

---

## Estrutura de Diretórios

```
project/
├── notebooks/
│   ├── 01_image_to_pointcloud.ipynb     # TripoSR: imagem → mesh densa → point cloud
│   ├── 02_inference.ipynb               # MeshAnything V2 + baselines
│   └── 03_evaluation.ipynb              # Métricas + tabelas + visualizações
├── src/
│   ├── metrics/                         # CD, ECD, NC, #V, #F, V_Ratio, F_Ratio
│   ├── visualization/                   # Comparação visual de meshes
│   └── utils/
│       └── io.py                        # Carregar/salvar meshes e point clouds
├── data/
│   ├── images/                          # Imagens próprias (novo dataset)
│   ├── pointclouds/                     # Point clouds gerados pelo TripoSR
│   └── meshes/
│       ├── ground_truth/                # Meshes densas do TripoSR
│       ├── meshanything_v2/             # Saída do modelo principal
│       └── baselines/
│           └── naive/                   # Saída do baseline naive
└── results/
    ├── tables/                          # Tabelas comparativas (CSV)
    └── figures/                         # Imagens comparativas
```

---

## Bibliotecas

| Biblioteca | Uso |
|------------|-----|
| **PyTorch** | Inferência dos modelos |
| **Open3D** | Manipulação de point clouds e meshes |
| **Trimesh** | Amostragem de points para métricas |
| **NumPy / SciPy** | Cálculo das métricas |
| **Matplotlib** | Visualizações |
| **Pandas** | Tabulação de resultados |

---

## Resultado Esperado

Tabela no formato do paper original (Tabela 2):

| Método | CD ↓ | ECD ↓ | NC ↑ | #V ↓ | #F ↓ | V_Ratio ↓ | F_Ratio ↓ |
|--------|------|-------|------|------|------|-----------|-----------|
| Baseline naive | — | — | — | — | — | — | — |
| **MeshAnything V2 (AMT)** | — | — | — | — | — | — | — |
