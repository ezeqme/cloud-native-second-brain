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
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Vlad Ungureanu", "Ali Monfre", "Palantir Technologies"]
sched_url: https://kccncna2023.sched.com/event/1R2m3/deploying-kubernetes-in-classified-environments-vlad-ungureanu-ali-monfre-palantir-technologies
youtube_search_url: https://www.youtube.com/results?search_query=Deploying+Kubernetes+in+Classified+Environments+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Deploying Kubernetes in Classified Environments - Vlad Ungureanu & Ali Monfre, Palantir Technologies

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Vlad Ungureanu, Ali Monfre, Palantir Technologies
- Schedule: https://kccncna2023.sched.com/event/1R2m3/deploying-kubernetes-in-classified-environments-vlad-ungureanu-ali-monfre-palantir-technologies
- Busca YouTube: https://www.youtube.com/results?search_query=Deploying+Kubernetes+in+Classified+Environments+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Deploying Kubernetes in Classified Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2m3/deploying-kubernetes-in-classified-environments-vlad-ungureanu-ali-monfre-palantir-technologies
- YouTube search: https://www.youtube.com/results?search_query=Deploying+Kubernetes+in+Classified+Environments+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-WEx_Uh0xAo
- YouTube title: Deploying Kubernetes in Classified Environments - Vlad Ungureanu & Ali Monfre, Palantir Technologies
- Match score: 0.742
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/deploying-kubernetes-in-classified-environments/-WEx_Uh0xAo.txt
- Transcript chars: 36085
- Keywords: software, actually, government, deploy, classified, networks, environments, little, operating, across, transfer, apollo, container, mentioned, management, places, access, specific

### Resumo baseado na transcript

thanks so much for joining us today we're super excited to be talking to you on this lovely Tuesday Morning of cubec con um before we get started we actually just had a quick question uh for the audience which is can I see a show of hands who is currently deploying software to classified networks today okay and then who is not and is kind of brand new okay all right we have a pretty good mix um so hopefully our content then is useful we have a couple

### Excerpt da transcript

thanks so much for joining us today we're super excited to be talking to you on this lovely Tuesday Morning of cubec con um before we get started we actually just had a quick question uh for the audience which is can I see a show of hands who is currently deploying software to classified networks today okay and then who is not and is kind of brand new okay all right we have a pretty good mix um so hopefully our content then is useful we have a couple of kind of introductory what does it mean what are the first set of challenges that you'll encounter when you try to deploy to these networks and then a little bit more in-depth lad's going to talk a lot about very specific technical problems that we faced in some of our Solutions so um hopefully content is relevant to you all um and then last thing I wanted to say before we get started is this talk is also part one of two um so we are speaking at the same time on Thursday as well about deploying kubernetes and other cncf Technologies to unclassified federal government environments for fed ramp and is 5 so par particularly for those of you who are a little bit newer to the government space feel free to check out that talk as well all right uh we wanted to start with just some brief introductions um talk a little bit about ourselves before we dive into the content um my name is Ali monrey I'm a senior architect of our federal government business at paler um what that means is essentially I oversee all of our Cloud architecture and Cloud deployments across our entire federal government portfolio um and I also lead business development for our Apollo product and fedstar program um which we're going to talk about more in this presentation hey folks my name is Vlad U I'm an engineering lead in the production infrastructure group uh since 2017 I've been leading the teams that deploy Kates and all the places that paler uh is running software that being classified cloud commercial Cloud on premise and Edge as well all right um brief overview of the agenda today um we are going to do just a a very brief sort of paler overview and introduction for those of you who are not familiar with paler as a company just talk a little bit about what we do and kind of how we got into this space and uh our our experience and expertise doing it um and then we're going to talk about some of the challenges you can see the subcategories here but um there are a lot of challenges to deploying in classified environments we're just going to
