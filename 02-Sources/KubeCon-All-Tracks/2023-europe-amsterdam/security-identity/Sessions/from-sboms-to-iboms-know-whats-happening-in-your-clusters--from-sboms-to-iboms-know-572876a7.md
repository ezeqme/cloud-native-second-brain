---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security", "Kubernetes Core"]
speakers: ["Ido Neeman", "Firefly"]
sched_url: https://kccnceu2023.sched.com/event/1HyYc/from-sboms-to-iboms-know-whats-happening-in-your-clusters-ido-neeman-firefly
youtube_search_url: https://www.youtube.com/results?search_query=From+SBOMs+to+IBOMs+-+Know+What%27s+Happening+in+Your+Clusters+CNCF+KubeCon+2023
slides: []
status: parsed
---

# From SBOMs to IBOMs - Know What's Happening in Your Clusters - Ido Neeman, Firefly

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ido Neeman, Firefly
- Schedule: https://kccnceu2023.sched.com/event/1HyYc/from-sboms-to-iboms-know-whats-happening-in-your-clusters-ido-neeman-firefly
- Busca YouTube: https://www.youtube.com/results?search_query=From+SBOMs+to+IBOMs+-+Know+What%27s+Happening+in+Your+Clusters+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre From SBOMs to IBOMs - Know What's Happening in Your Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYc/from-sboms-to-iboms-know-whats-happening-in-your-clusters-ido-neeman-firefly
- YouTube search: https://www.youtube.com/results?search_query=From+SBOMs+to+IBOMs+-+Know+What%27s+Happening+in+Your+Clusters+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=of6HC26f4i4
- YouTube title: From SBOMs to IBOMs - Know What's Happening in Your Clusters - Ido Neeman, Firefly
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/from-sboms-to-iboms-know-whats-happening-in-your-clusters/of6HC26f4i4.txt
- Transcript chars: 24683
- Keywords: infrastructure, understand, security, software, s-bomb, inventory, servers, important, server, native, entire, running, platform, configuration, version, everything, terraform, environment

### Resumo baseado na transcript

thank you for joining my talk from s-bombs to eye bombs know what's happening in your clusters first let's start with the most important thing what's in it for you why should you stay here and not grab the next cup of coffee I know I had one too many so first we start by understanding why I bomb which stands for infrastructure bill of materials is crucial for security but also for any platform efficiency then we're going to Define ibom and understand why we should all care about

### Excerpt da transcript

thank you for joining my talk from s-bombs to eye bombs know what's happening in your clusters first let's start with the most important thing what's in it for you why should you stay here and not grab the next cup of coffee I know I had one too many so first we start by understanding why I bomb which stands for infrastructure bill of materials is crucial for security but also for any platform efficiency then we're going to Define ibom and understand why we should all care about it next we'll talk about what's the implications in terms of attack service for ibom and later learn how ibom can help us all learn how to control our clouds better so um who are we my name is Edo Niemann I'm the co-founder and CEO at the company called Firefly we're doing Cloud Asset Management I spent almost almost 12 years in the Israeli cyber intelligence Force um then LED technology for a permanent hedge fund work for a startup in in the serverless field and with me today should be Cindy Blake fireflies VP of marketing but this is the first infrastructure fail all right so just like I bomb and s-bomb we created an amazing we hope amazing deck for you but Cindy couldn't be here so the software the service worked well but the infrastructure failed and if we could do the bomb the bill of material for the infrastructure we could have prepped better for this call so so it would be only me but I'll try to make up for Sydney's absence so let's start with the basics for the past few years s-bomb is being crazy like a very hot buzzword so I'm I'm sure most of you heard about it many many times so I don't want to reinvent the will and talk about what is as Mom and why it's important so I asked the most the smartest thing I know um chat GPT what sbomb is all about and it gave me a very elaborate answer so let's let's take the key part of it it says something about software of materials complete inventory of all software components it has all third-party software open source libraries and other components this is where most of us are focusing our current s-bomb um efforts and Endeavors and then the s-bomb is essential component for software supply chain security supply chain is fantastic personally I'm I'm really excited about this build and you need to list all the third-party components right so what basically says let's understand what our services our software is comprised of let's list all the open source all the dependencies and the supply chain and understand um what we have in our
