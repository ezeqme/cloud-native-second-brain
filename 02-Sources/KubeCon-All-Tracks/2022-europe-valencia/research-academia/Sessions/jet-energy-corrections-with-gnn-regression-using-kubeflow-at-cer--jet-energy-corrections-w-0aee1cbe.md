---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Research + Academia"
themes: ["Sustainability"]
speakers: ["Daniel Holmberg", "Dejan Golubovic", "CERN"]
sched_url: https://kccnceu2022.sched.com/event/ytqv/jet-energy-corrections-with-gnn-regression-using-kubeflow-at-cern-daniel-holmberg-dejan-golubovic-cern
youtube_search_url: https://www.youtube.com/results?search_query=Jet+Energy+Corrections+with+GNN+Regression+using+Kubeflow+at+CERN+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Jet Energy Corrections with GNN Regression using Kubeflow at CERN - Daniel Holmberg & Dejan Golubovic, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Research + Academia]]
- Temas: [[Sustainability]]
- País/cidade: Spain / Valencia
- Speakers: Daniel Holmberg, Dejan Golubovic, CERN
- Schedule: https://kccnceu2022.sched.com/event/ytqv/jet-energy-corrections-with-gnn-regression-using-kubeflow-at-cern-daniel-holmberg-dejan-golubovic-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Jet+Energy+Corrections+with+GNN+Regression+using+Kubeflow+at+CERN+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Jet Energy Corrections with GNN Regression using Kubeflow at CERN.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytqv/jet-energy-corrections-with-gnn-regression-using-kubeflow-at-cern-daniel-holmberg-dejan-golubovic-cern
- YouTube search: https://www.youtube.com/results?search_query=Jet+Energy+Corrections+with+GNN+Regression+using+Kubeflow+at+CERN+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iqbsbXZDjs8
- YouTube title: Jet Energy Corrections with GNN Regression using Kubeflow @ CERN - Daniel Holmberg & Dejan Golubovic
- Match score: 0.86
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/jet-energy-corrections-with-gnn-regression-using-kubeflow-at-cern/iqbsbXZDjs8.txt
- Transcript chars: 18260
- Keywords: learning, machine, energy, particles, particle, physics, kubeflow, network, parameters, experiment, models, multiple, tensorboard, triton, predictions, called, algorithms, specific

### Resumo baseado na transcript

hello everyone thank you for being here to listen to our presentation my name is dan i'm here with my colleague daniel we both work at cern and today we are going to share a use case of machine learning application in high energy physics and you know to show how we can scale such workloads with cube floor a bit of introduction about cern cern is a particle physics research organization located in switzerland its mission to is to expand the knowledge of the universe and how subatomic particles

### Excerpt da transcript

hello everyone thank you for being here to listen to our presentation my name is dan i'm here with my colleague daniel we both work at cern and today we are going to share a use case of machine learning application in high energy physics and you know to show how we can scale such workloads with cube floor a bit of introduction about cern cern is a particle physics research organization located in switzerland its mission to is to expand the knowledge of the universe and how subatomic particles interact with each other what their properties are uh it's operating the largest particle physics lab in the world and it is an international collaboration of over 17 000 part-time and full-time employees from over 110 nationalities cern is studying the subatomic particles and it is doing that through with the help of large hadron collider a large cardron collider is the largest particle accelerator in the world and one of the most massive machines ever built it is a 27 kilometer ring of superconducting magnets that is located 100 meters underground at the swiss french border uh it works by accelerating the beams of protons from opposite directions until they meet the until they approach the speed of light and then these beams collide at four collision points called uh detectors or experiments and this is where all the data is uh gathered and analyzed uh here we can see our globe the the exhibition building at cern here is an illustration of the lhc magnets and here we can see the cms experiment and we can see the magnitude of the experiment now a little bit about machine learning and cube flow at sir um there uh the lhc produces a lot of data there are 40 million collisions happening every second in the lhc and even after filtering that translates to around 90 petabytes of data produced by all experiments per year so there is a potential for machine learning in different stages we can apply machine learning in data acquisition or later in the offline analysis and we can utilize machine learnings to machine learning algorithms to find the patterns of interactions between particles uh in this slide i will cover a couple of examples of machine learning uh applications at cern and later daniel will cover one specific use case in more detail in data acquisition we have uh at the cms experiment we have uh so-called trigger mechanisms these mechanisms are extremely important because they select uh which of which collisions are interesting to store and process further it is
