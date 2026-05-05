---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["AI ML", "SRE Reliability", "Sustainability"]
speakers: ["Atanas Atanasov", "Intel", "Daniel Wilson", "Boston University"]
sched_url: https://kccncna2023.sched.com/event/1R2tJ/environmentally-sustainable-ai-via-power-aware-batch-scheduling-atanas-atanasov-intel-daniel-wilson-boston-university
youtube_search_url: https://www.youtube.com/results?search_query=Environmentally+Sustainable+AI+via+Power-Aware+Batch+Scheduling+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Environmentally Sustainable AI via Power-Aware Batch Scheduling - Atanas Atanasov, Intel & Daniel Wilson, Boston University

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Sustainability]]
- País/cidade: United States / Chicago
- Speakers: Atanas Atanasov, Intel, Daniel Wilson, Boston University
- Schedule: https://kccncna2023.sched.com/event/1R2tJ/environmentally-sustainable-ai-via-power-aware-batch-scheduling-atanas-atanasov-intel-daniel-wilson-boston-university
- Busca YouTube: https://www.youtube.com/results?search_query=Environmentally+Sustainable+AI+via+Power-Aware+Batch+Scheduling+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Environmentally Sustainable AI via Power-Aware Batch Scheduling.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2tJ/environmentally-sustainable-ai-via-power-aware-batch-scheduling-atanas-atanasov-intel-daniel-wilson-boston-university
- YouTube search: https://www.youtube.com/results?search_query=Environmentally+Sustainable+AI+via+Power-Aware+Batch+Scheduling+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2GQnzZhmGRc
- YouTube title: Environmentally Sustainable AI via Power-Aware Batch Scheduling - Atanas Atanasov & Daniel Wilson
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/environmentally-sustainable-ai-via-power-aware-batch-scheduling/2GQnzZhmGRc.txt
- Transcript chars: 33981
- Keywords: basically, application, container, applications, management, training, actually, infrastructure, slowdown, systems, energy, control, working, software, device, resource, capping, performance

### Resumo baseado na transcript

hello everyone uh my name is Daniel Wilson and I'm presenting uh along with the tanas uh we're going to talk about environmentally sustainable AI via powerware uh batch scheduling so I've been doing this work as an intern with Intel uh under the leadership of atonis and Chris calupo uh and done this with the support of all of these other people uh run the the gopm team over at Intel so uh let's uh begin so for some of the background about why we're looking into this uh

### Excerpt da transcript

hello everyone uh my name is Daniel Wilson and I'm presenting uh along with the tanas uh we're going to talk about environmentally sustainable AI via powerware uh batch scheduling so I've been doing this work as an intern with Intel uh under the leadership of atonis and Chris calupo uh and done this with the support of all of these other people uh run the the gopm team over at Intel so uh let's uh begin so for some of the background about why we're looking into this uh is basically just that AI workloads demand a lot of power um one of the things that you might notice when you look at the different types of things that are happening in these systems is that the overall impact in total of say energy consumption will often be pointing at things like inference however when you're looking at the the single run impact of an individual uh sort of run of doing something with your AI models it's the uh the training side that really has the really heavy impact all at one point in time so this gives us a big uh focal point on which we can put our uh power management decisions to try and have a large impact anyways so one of the things that we found is this project uh that uh I have been working on in my internship gopm uh where it focuses on power management decisions in HPC systems a lot of the things that we've been looking at in HBC are also relevant in cloud computing systems in particular with Bach oriented training in AI models so one of the key bits that I really want to emphasize to start here is that some workloads use power more effectively than others the way this is kind of visualized down here on the power cap diagram in the bottom right is that if you have uh basically a power cap that goes from some high number to some low number you're going to see that the runtime increases for your applications now the amount that it increases uh for an individual application is actually application specific uh it depends on the different components you're using with that Computing system and how the application uses those different components um so another Point here is that there are some estimates that place training a single uh llm model ranging from on the order of like 300 to 600,000 tons of CO2 so this energy impact ultimately uh contributes towards high carbon impact as well so these are a lot of motivations we have for uh investigating how we can use power control to help modulate systems so uh in order to work toward that uh we're working for a software s
