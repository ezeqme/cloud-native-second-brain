---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Reliability + Operational Continuity"
themes: ["SRE Reliability"]
speakers: ["Steve McGhee", "Ameer Abbas", "Google"]
sched_url: https://kccnceu2023.sched.com/event/1HyZa/archetypes-for-reliable-systems-steve-mcghee-ameer-abbas-google
youtube_search_url: https://www.youtube.com/results?search_query=Archetypes+for+Reliable+Systems+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Archetypes for Reliable Systems - Steve McGhee & Ameer Abbas, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Steve McGhee, Ameer Abbas, Google
- Schedule: https://kccnceu2023.sched.com/event/1HyZa/archetypes-for-reliable-systems-steve-mcghee-ameer-abbas-google
- Busca YouTube: https://www.youtube.com/results?search_query=Archetypes+for+Reliable+Systems+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Archetypes for Reliable Systems.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyZa/archetypes-for-reliable-systems-steve-mcghee-ameer-abbas-google
- YouTube search: https://www.youtube.com/results?search_query=Archetypes+for+Reliable+Systems+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OdLnC8sjPCI
- YouTube title: Archetypes for Reliable Systems - Steve McGhee & Ameer Abbas, Google
- Match score: 0.74
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/archetypes-for-reliable-systems/OdLnC8sjPCI.txt
- Transcript chars: 35525
- Keywords: region, platform, archetypes, archetype, product, actually, trying, google, application, change, clusters, failure, reliability, applications, global, active, products, running

### Resumo baseado na transcript

all right we're gonna get started we have a lot to cover thank you so much for coming thank you for your time uh my name is Amir Abbas I'm a product manager at Google I focus on application modernization service mesh also part of the istio steering committee for all the istio folks out there I'll be I'll be at the istio booth later I've been with Google for about six years uh and now I focus on reliability and multi-cluster architecture patterns Steve and I'm Steve McGee uh

### Excerpt da transcript

all right we're gonna get started we have a lot to cover thank you so much for coming thank you for your time uh my name is Amir Abbas I'm a product manager at Google I focus on application modernization service mesh also part of the istio steering committee for all the istio folks out there I'll be I'll be at the istio booth later I've been with Google for about six years uh and now I focus on reliability and multi-cluster architecture patterns Steve and I'm Steve McGee uh I'm a reliability Advocate which is a title I just made up part of devrel but I used to be an SRE for a long time so I sort of like feel like I am just an SRE uh has anyone here an SRE raise your hand yeah my people right on um so I I worked on a bunch of services like Android and YouTube Cloud for a while and then I left I left Google I became a customer so I I moved to California I helped this company move from on-prem you know monolith you know big knock all this stuff onto the cloud and it was difficult let me tell you it was very difficult I learned a lot in that year um so I actually came back to Google to basically help more companies go through that process because uh I don't think it's easy to go through it alone so I'm hoping we can show you guys a couple ideas here today to help you build more reliable services and just kind of make the internet more reliable as a whole the first step uh question you can answer this in your head you can raise your hand whatever um the question is can you build four or nine services on top of three nines infrastructure can you is it possible so my favorite thing about this question is not what the answer is it's the fact that every time I ask a room full of people I get half yes and half no not necessarily like left and right but like half and half you know um I actually asked that question at srecon here in Amsterdam last year still half yes half no so it's not a straightforward answer so this question is kind of weird so uh to help understand what I mean by all this and and why I think I think the answer is yes I'm hoping that uh by the end of the talk today you will agree with me if you don't already but to help understand that and we're going to use a couple uh kind of symbols and and uh analogies I guess so first up we have these uh pyramids uh this is a little abstract but bear with me uh the way that we have done reliability in the past for a very long time was like the pyramids in Giza you know big giant thing very stable base the thin
