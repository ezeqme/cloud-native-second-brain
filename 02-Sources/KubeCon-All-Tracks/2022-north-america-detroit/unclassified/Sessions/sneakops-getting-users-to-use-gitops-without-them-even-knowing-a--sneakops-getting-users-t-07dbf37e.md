---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Unclassified"
themes: ["GitOps Delivery"]
speakers: ["Éamon Ryan", "Hedley Simons", "Grafana Labs"]
sched_url: https://kccncna2022.sched.com/event/182HI/sneakops-getting-users-to-use-gitops-without-them-even-knowing-about-it-eamon-ryan-hedley-simons-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=SneakOps+%E2%80%93+Getting+Users+To+Use+GitOps+Without+Them+Even+Knowing+About+It%21+CNCF+KubeCon+2022
slides: []
status: parsed
---

# SneakOps – Getting Users To Use GitOps Without Them Even Knowing About It! - Éamon Ryan & Hedley Simons, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Detroit
- Speakers: Éamon Ryan, Hedley Simons, Grafana Labs
- Schedule: https://kccncna2022.sched.com/event/182HI/sneakops-getting-users-to-use-gitops-without-them-even-knowing-about-it-eamon-ryan-hedley-simons-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=SneakOps+%E2%80%93+Getting+Users+To+Use+GitOps+Without+Them+Even+Knowing+About+It%21+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre SneakOps – Getting Users To Use GitOps Without Them Even Knowing About It!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182HI/sneakops-getting-users-to-use-gitops-without-them-even-knowing-about-it-eamon-ryan-hedley-simons-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=SneakOps+%E2%80%93+Getting+Users+To+Use+GitOps+Without+Them+Even+Knowing+About+It%21+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yQE1Lqt01RI
- YouTube title: SneakOps – Getting Users To Use GitOps Without Them Even Knowing... - Éamon Ryan & Hedley Simons
- Match score: 0.934
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/sneakops-getting-users-to-use-gitops-without-them-even-knowing-about-i/yQE1Lqt01RI.txt
- Transcript chars: 33437
- Keywords: actually, grafana, dashboards, dashboard, folder, production, terraform, github, atlantis, environment, question, instance, little, ensure, running, everything, version, obviously

### Resumo baseado na transcript

uh welcome to the talk uh it's uh going to get well easier a bit okay um it's gonna be a little darker in here as uh we were just warned uh the reason for that is of course we're using a dark very dark slide theme uh which is actually our company slide theme so that's just kind of how it is and the lights are kind of washing it out so pretty enjoy the darkness for a little bit uh commit you can have a nap if you clean production one and we want to provision things across the way get UPS but the challenge is that a lot of our users don't actually use git on a day-to-day basis so we need to ensure that we did something that would allow them

### Excerpt da transcript

uh welcome to the talk uh it's uh going to get well easier a bit okay um it's gonna be a little darker in here as uh we were just warned uh the reason for that is of course we're using a dark very dark slide theme uh which is actually our company slide theme so that's just kind of how it is and the lights are kind of washing it out so pretty enjoy the darkness for a little bit uh commit you can have a nap if you want like we're not gonna be mad about it uh I was going to make a joke about uh it's great to see there's so many people attending but now I can't see anybody anymore so you know I'm just going to assume you're all still here uh so the talk is uh snake Ops getting youthers you use get up so that's even knowing about it and my name is Eamonn Ryan I'm a principal field engineer at confined labs and I'm joined here by my partner in crime um get a note that does we support the Solution Services or the sales engineers at the funnel apps we ensure that they are able to get the the technical debt that they need for some of their engagements they know a lot about the Health products are used we know a lot of that has products are architected we also write workshops we write an open material and we also uh built and maintain the demo kit and we're talking about in a little bit now so this is uh kind of well am I too close to something I can't really tell is it you know is it this one okay all right let's use better okay so this is a very uh basic view of the environment uh that has mentioned called the demo kit that we support uh it essentially is a gke cluster uh with uh a whole bunch of stuff deployed on top of it so we've got a large uh buzzing history just turn this one off that's all it's up okay anyway um so it's this large instance it's got grafana in there as I'm sure everyone here is familiar with grafana maybe not familiar with all the other stuff it connects to lots of people only connected to one or two things uh but because we are a Groupon labs and one of the teams we support uh is involved in uh showing demos for what grafana can speak to we have it hooked up to literally everything we possibly can so on the left side it's uh Prometheus as well as all the other projects and products that grafana has like on-call and mimir and incident and Loki and Tempo and ML and k6 on the right hand side we have all these third party things that we can also connect up to uh especially on like like the Enterprise version of our stuff like servicenow and Ora
