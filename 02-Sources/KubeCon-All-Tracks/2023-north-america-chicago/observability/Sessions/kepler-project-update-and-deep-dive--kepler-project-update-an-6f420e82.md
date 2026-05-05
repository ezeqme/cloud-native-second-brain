---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Observability"
themes: ["Observability"]
speakers: ["Marcelo Amaral", "Tatsuhiro Chiba", "IBM"]
sched_url: https://kccncna2023.sched.com/event/1R2rh/kepler-project-update-and-deep-dive-marcelo-amaral-tatsuhiro-chiba-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Kepler%3A+Project+Update+and+Deep+Dive+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kepler: Project Update and Deep Dive - Marcelo Amaral & Tatsuhiro Chiba, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Chicago
- Speakers: Marcelo Amaral, Tatsuhiro Chiba, IBM
- Schedule: https://kccncna2023.sched.com/event/1R2rh/kepler-project-update-and-deep-dive-marcelo-amaral-tatsuhiro-chiba-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Kepler%3A+Project+Update+and+Deep+Dive+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kepler: Project Update and Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2rh/kepler-project-update-and-deep-dive-marcelo-amaral-tatsuhiro-chiba-ibm
- YouTube search: https://www.youtube.com/results?search_query=Kepler%3A+Project+Update+and+Deep+Dive+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pDybCLlQrXQ
- YouTube title: Kepler: Project Update and Deep Dive - Marcelo Amaral & Tatsuhiro Chiba, IBM
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kepler-project-update-and-deep-dive/pDybCLlQrXQ.txt
- Transcript chars: 25881
- Keywords: kepler, consumption, energy, matrix, memory, overhead, running, resource, collect, utilization, expose, metrix, metric, models, process, gpu, collecting, future

### Resumo baseado na transcript

all right uh let's get started okay so hello everyone um thank you for coming our session or keep update so uh I'm CH chra from nav research and uh today we're not going to talk about CER and the keer itself and also there are some project update on the Deep dive on the recent topics so all right so let me get first for the um briefly introduce some our introduction and the motivation and also the fs going on and the Capal deployment over the last couple

### Excerpt da transcript

all right uh let's get started okay so hello everyone um thank you for coming our session or keep update so uh I'm CH chra from nav research and uh today we're not going to talk about CER and the keer itself and also there are some project update on the Deep dive on the recent topics so all right so let me get first for the um briefly introduce some our introduction and the motivation and also the fs going on and the Capal deployment over the last couple months or last years and what's going on next so all right so before I jump into the keper so you know all know about your sity is a top interest the top con uh concern about your companies right and uh this kind of the sustainability topics is rapidly growing and focusing on many organizations and uh yeah you know CTO CEO everyone want to in introduce or the Su future in their product and that's behind that right so why they want to know about to focus on their sustainabilities is there the that there are many reason is there many kind of the climate changes happen in the world and then so we want to reduce the global um emissions and gas right so that's is the requirement from the government and companies and what they want to track and all of the energy consumptions and carbon footprint reductions right so that's uh behind one of the reason right so but uh the almost of data centers is consumed all many wat right is you can imagine the 200 25 500 Katt hours electricities is I we canot I canot IM but it takes very huge resources uh in the data centers I heard this com almost same of the ERS uh the day uh usage right so really big uh usage um the at the same times it's also the the data centers F uh data center using for the this energies right uh it's time order computer energy problem is real uh we know many gpus running on the uh the data centers and the and many AI workr consumes of the data center energies especially for the gpus um CH gpts and creating some uh large rage models it consumes many gpus all all over days or all weeks or maybe there over the months continuously that makes a lot of the energy consumption in the data centers and also as well as influence workl also consumes so the growing the demand of the resources Computing resources and AI workloads influencing trainings that makes a lot of the power uh pressure to the DAT center right so to solve that we have two option uh one option is creating a new hardware uh to reducer and energy consumptions as much as possible that's the one key
