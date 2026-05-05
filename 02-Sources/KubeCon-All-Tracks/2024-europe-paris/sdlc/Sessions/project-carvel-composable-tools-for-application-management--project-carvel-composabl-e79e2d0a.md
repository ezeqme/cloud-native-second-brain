---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "SDLC"
themes: ["SDLC"]
speakers: ["Daniel Garnier-Moiroux", "Soumik Majumder", "Broadcom"]
sched_url: https://kccnceu2024.sched.com/event/1YeRj/project-carvel-composable-tools-for-application-management-daniel-garnier-moiroux-soumik-majumder-broadcom
youtube_search_url: https://www.youtube.com/results?search_query=Project+Carvel%3A+Composable+Tools+for+Application+Management+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Project Carvel: Composable Tools for Application Management - Daniel Garnier-Moiroux & Soumik Majumder, Broadcom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[SDLC]]
- Temas: [[SDLC]]
- País/cidade: France / Paris
- Speakers: Daniel Garnier-Moiroux, Soumik Majumder, Broadcom
- Schedule: https://kccnceu2024.sched.com/event/1YeRj/project-carvel-composable-tools-for-application-management-daniel-garnier-moiroux-soumik-majumder-broadcom
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Carvel%3A+Composable+Tools+for+Application+Management+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Project Carvel: Composable Tools for Application Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRj/project-carvel-composable-tools-for-application-management-daniel-garnier-moiroux-soumik-majumder-broadcom
- YouTube search: https://www.youtube.com/results?search_query=Project+Carvel%3A+Composable+Tools+for+Application+Management+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1u5LtsJqyrA
- YouTube title: Project Carvel: Composable Tools for Application Management
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/project-carvel-composable-tools-for-application-management/1u5LtsJqyrA.txt
- Transcript chars: 33898
- Keywords: package, config, values, configuration, deployment, version, bundle, resources, cluster, called, change, deploy, everything, coupon, images, supply, output, actually

### Resumo baseado na transcript

hey I hope I'm audible so we know it's the last day of the conference and everyone has a lot to think about you're pretty saturated but we hoping we can give you like a little bit more right so we're going to be talking about project carel today but before we jump into that a little bit about ourselves so my name is somic I work at team tanzu atcom and I mainly work with developer experience tooling and a part of my job is to maintain the project here uh with image package so we do image package image package push into a bundle a bundle is a target oi image I'm going to push it to my local registry 5,000 coupon uh caral and then the tag will be demo right and cap so you can sort of see the same diff that we saw like earlier in the demo right right and so this is a a developer friendly workflow but of course uh under the hood what it's really doing is creating custom resources on to having a more G opsy workflow to manage like all of your infrastructure right okay um we're almost at time um before we we close this out um there's the demo for the the repository for this demo is on the internet on the

### Excerpt da transcript

hey I hope I'm audible so we know it's the last day of the conference and everyone has a lot to think about you're pretty saturated but we hoping we can give you like a little bit more right so we're going to be talking about project carel today but before we jump into that a little bit about ourselves so my name is somic I work at team tanzu atcom and I mainly work with developer experience tooling and a part of my job is to maintain the project we're going to be talking about today KL and I'm here with my colleague and hi I'm Daniel as you can tell by my name and probably not my accent I'm from here um I work in the tanzo team and the spring team I do Java for a living don't judge me and here are socials um you know feel free to reach out if you have questions if you have feedback we love to engage is the font size all right for the people in the back of the room yeah all right a little bit more this cool all right all right so carvo so um I guess we can really hop real quick to the website maybe so Carell started off as like a set of composable single purpose tools and they sort of come together to help you sort of manage your applications and ship them to your end user right I guess the keywords here are reliable single purpose and composable and when we say reliable we mean that it's the tools are important like they're very repeatable in nature and if we scroll down a bit we'll be taking a look at the tools you're talking about today so we'll mainly be talking about the first fight tools you see here and uh not the experimental ones so to sort of uh I guess the best way to explore the tools is to get your hands dirty right and that's exactly what we'll be doing so maybe we can hop back to the terminal all right let's get let's get rolling so what do we start with right so we'll be starting off with YT YT stands for yaml templating Tool right and that's exactly what it does the templates yaml but what sort of sets YT aside is that YT understands yaml a data structure which means that you can shape yaml in unique ways and everything that goes into YT is valid yaml and everything that comes out of it is the have valid yam so maybe you could take a quick look like we have some configuration to play around with so I want to point out that any any yaml is valid y That's valid is okay for ytt right um so if I do this I can pass it into ytt and it it works it doesn't have to be kubernetes resources so if you want to template your GitHub actions your config f
