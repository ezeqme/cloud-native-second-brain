---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Rajas Kakodkar", "Broadcom", "Kevin Klues", "NVIDIA", "Joseph Sandoval", "Adobe", "Ricardo Rocha", "CERN", "Dawn Chen", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7qR/from-vectors-to-pods-integrating-ai-with-cloud-native-rajas-kakodkar-broadcom-kevin-klues-nvidia-joseph-sandoval-adobe-ricardo-rocha-cern-dawn-chen-google
youtube_search_url: https://www.youtube.com/results?search_query=From+Vectors+to+Pods%3A+Integrating+AI+with+Cloud+Native+CNCF+KubeCon+2024
slides: []
status: parsed
---

# From Vectors to Pods: Integrating AI with Cloud Native - Rajas Kakodkar, Broadcom; Kevin Klues, NVIDIA; Joseph Sandoval, Adobe; Ricardo Rocha, CERN; Dawn Chen, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Rajas Kakodkar, Broadcom, Kevin Klues, NVIDIA, Joseph Sandoval, Adobe, Ricardo Rocha, CERN, Dawn Chen, Google
- Schedule: https://kccncna2024.sched.com/event/1i7qR/from-vectors-to-pods-integrating-ai-with-cloud-native-rajas-kakodkar-broadcom-kevin-klues-nvidia-joseph-sandoval-adobe-ricardo-rocha-cern-dawn-chen-google
- Busca YouTube: https://www.youtube.com/results?search_query=From+Vectors+to+Pods%3A+Integrating+AI+with+Cloud+Native+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre From Vectors to Pods: Integrating AI with Cloud Native.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qR/from-vectors-to-pods-integrating-ai-with-cloud-native-rajas-kakodkar-broadcom-kevin-klues-nvidia-joseph-sandoval-adobe-ricardo-rocha-cern-dawn-chen-google
- YouTube search: https://www.youtube.com/results?search_query=From+Vectors+to+Pods%3A+Integrating+AI+with+Cloud+Native+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=j67Xv_ywFZY
- YouTube title: From Vectors to Pods: Integrating AI with Cloud Native - Panel
- Match score: 1.026
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/from-vectors-to-pods-integrating-ai-with-cloud-native/j67Xv_ywFZY.txt
- Transcript chars: 35383
- Keywords: resource, scheduling, native, actually, around, challenges, workloads, infrastructure, everyone, machine, gpu, cost, resources, challenge, learning, projects, question, access

### Resumo baseado na transcript

all right welcome everyone uh we are here at the from vectors to pods integrating AI with Cloud native panel discussion um I am rajas kakodkar I work at broadcom for all things kubernetes and I'm also a tech lead for CNC of tech rtime active in the working group artificial intelligence Community um my panelists over here they need no introduction but for the sake of completeness will quickly go around and get a quick intro from everyone so Ricardo you want to start yeah I can start so

### Excerpt da transcript

all right welcome everyone uh we are here at the from vectors to pods integrating AI with Cloud native panel discussion um I am rajas kakodkar I work at broadcom for all things kubernetes and I'm also a tech lead for CNC of tech rtime active in the working group artificial intelligence Community um my panelists over here they need no introduction but for the sake of completeness will quickly go around and get a quick intro from everyone so Ricardo you want to start yeah I can start so my name is Ricardo I'm uh I lead the platform infrastructure team at CERN handling everything related to Cloud native and machine learning platforms I'm also in the cncf technical oversight committee and the end user technical advisory report I'm Joseph sanal I'm the principal product manager at Adobe for our underlying kubernetes infrastructure I'm also a member of the cnfn user techic Advisory Board Sig release manager associate and also cucon co-chair I'm Kevin Clues I'm from Nvidia I work on the team that enables GPU support in containers and kubernetes uh one of the main projects I'm pushing right now is uh Dr Dynamic resource allocation and I'm also a Sig node maintainer my name is donen from Google um and I'm one of the original uh founding engineer for uh for the cetes uh 10 years ago and also I'm the one of the tech lead uh for the S Lo and since the Inception the co9 is signal founded and also I'm the one of the tech lead for the gke for last 10 years all right cool uh I think this Cube con uh similar to last couple of cubec conss AI has been buzzing around uh someone someone told me yesterday that almost every talk that they went to regarding AI Q was was like something that they couldn't miss out on uh Ricardo had a had an amazing live demo for the Keynotes yesterday on multiq uh so running AI workloads on kubernetes has been like something um some something that has proven that cloud native is like the def facto choice of infrastructure when it comes to these workloads they've gone from like Niche workloads to uh something that everyone wants to run right now but in this panel we're going to flip things around this discussion is going to be to talk about the other side of things on integrating AI with Cloud native uh I don't know how that's going to be uh we'll just try to pick everyone's brain over here see how that goes and just to uh you know kick things off uh so quickly if we can just go around the uh table like around everyone and like quickly gets your get
