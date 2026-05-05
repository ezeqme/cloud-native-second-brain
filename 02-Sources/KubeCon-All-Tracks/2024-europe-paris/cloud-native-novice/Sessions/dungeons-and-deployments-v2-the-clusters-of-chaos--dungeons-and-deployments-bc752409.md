---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Cloud Native Novice"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Kat Cosgrove", "Dell Technologies", "Noah Abrahams", "Oracle", "Seth McCombs", "AcuityMD", "Ian Coldwater", "Independent", "Natali Vlatko", "Cisco"]
sched_url: https://kccnceu2024.sched.com/event/1YeMv/dungeons-and-deployments-v2-the-clusters-of-chaos-kat-cosgrove-dell-technologies-noah-abrahams-oracle-seth-mccombs-acuitymd-ian-coldwater-independent-natali-vlatko-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Dungeons+and+Deployments+V2%3A+The+Clusters+of+Chaos+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Dungeons and Deployments V2: The Clusters of Chaos - Kat Cosgrove, Dell Technologies; Noah Abrahams, Oracle; Seth McCombs, AcuityMD; Ian Coldwater, Independent; Natali Vlatko, Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Kat Cosgrove, Dell Technologies, Noah Abrahams, Oracle, Seth McCombs, AcuityMD, Ian Coldwater, Independent, Natali Vlatko, Cisco
- Schedule: https://kccnceu2024.sched.com/event/1YeMv/dungeons-and-deployments-v2-the-clusters-of-chaos-kat-cosgrove-dell-technologies-noah-abrahams-oracle-seth-mccombs-acuitymd-ian-coldwater-independent-natali-vlatko-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Dungeons+and+Deployments+V2%3A+The+Clusters+of+Chaos+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Dungeons and Deployments V2: The Clusters of Chaos.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMv/dungeons-and-deployments-v2-the-clusters-of-chaos-kat-cosgrove-dell-technologies-noah-abrahams-oracle-seth-mccombs-acuitymd-ian-coldwater-independent-natali-vlatko-cisco
- YouTube search: https://www.youtube.com/results?search_query=Dungeons+and+Deployments+V2%3A+The+Clusters+of+Chaos+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EWJ6Ih_bQbo
- YouTube title: Dungeons and Deployments V2: The Clusters of Chaos
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/dungeons-and-deployments-v2-the-clusters-of-chaos/EWJ6Ih_bQbo.txt
- Transcript chars: 29865
- Keywords: cluster, access, looking, probably, inside, telescope, actually, running, certificate, everyone, security, server, everybody, sounds, character, cleric, little, bucket

### Resumo baseado na transcript

hello everyone and welcome to Dungeons and deployments module two the clusters of chaos uh we are not in any way affiliated with the company downstairs it apparently liked our first talk so much that they used this phrase on their Booth we had nothing to do with that um how this talk is going to work uh so this is the cloud native novice track we're here to teach you Basics about security uh things you should have in mind be concerned with when you're managing a kubernetes environment

### Excerpt da transcript

hello everyone and welcome to Dungeons and deployments module two the clusters of chaos uh we are not in any way affiliated with the company downstairs it apparently liked our first talk so much that they used this phrase on their Booth we had nothing to do with that um how this talk is going to work uh so this is the cloud native novice track we're here to teach you Basics about security uh things you should have in mind be concerned with when you're managing a kubernetes environment we're not going to go deep we're not going to dive into the concepts particularly hard uh but we are actually going to try to play play the game while we're up here we all got dice uh some of us have character sheets um we're going to break the fourth wall for explanations and expositions so if you see us standing up that's really us talking to you uh but everything else we're going to try and keep within the table uh and it'll be sort of like watching a sitcom but but we won't be funny thank you thank you uh as we said laughter's fine and lots of bad jokes we expect you will groan and you're locked in here with us so hello everyone it's been a few weeks since we managed to play last time uh let's remind everyone of who we are I'm Noah I'm the DM for your session okay the DM is is basically the API server in this context uh in the previous session we talked about what it looks like to deal with requests and storing information and things like that uh but this is a security theme talk so what you want to pay attention to is whether or not I can be compromised now a real DM can be bribed with snacks very easily uh thank you yeah you're so welcome uh but a API server does not like chicken crimpy uh so the question to you to keep in mind is what can you offer an API server that would be accepted hi gang good to see you again it's me era the tling grave cleric my name is also Natalie and I'm uh a Sig dos co-chair for kubernetes and um oh one sec one sec cosplay I'm the cleric hey that's my one joke okay sick um so for folks who don't know a cleric is a Healer and if you remember part one of this talk um we are going to think about that as being like your cicd system uh which means you're or I am responsible for Providence defending the pipeline um and the chain of healing supplies in this party cicd is much like a grave cleric which is what I am in that there there is potential for psychic damage to all of you to all of us definitely by the end of this talk oh it's you yeah hi uh
