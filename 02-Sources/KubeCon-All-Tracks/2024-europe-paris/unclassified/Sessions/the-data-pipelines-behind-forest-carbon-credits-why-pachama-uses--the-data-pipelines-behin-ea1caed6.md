---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["Storage Data", "Sustainability"]
speakers: ["Bernhard Stadlbauer", "Pachama"]
sched_url: https://kccnceu2024.sched.com/event/1YeNk/the-data-pipelines-behind-forest-carbon-credits-why-pachama-uses-flyte-to-orchestrate-workflows-bernhard-stadlbauer-pachama
youtube_search_url: https://www.youtube.com/results?search_query=The+Data+Pipelines+Behind+Forest+Carbon+Credits+%E2%80%93+Why+Pachama+Uses+Flyte+to+Orchestrate+Workflows+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Data Pipelines Behind Forest Carbon Credits – Why Pachama Uses Flyte to Orchestrate Workflows - Bernhard Stadlbauer, Pachama

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[Storage Data]], [[Sustainability]]
- País/cidade: France / Paris
- Speakers: Bernhard Stadlbauer, Pachama
- Schedule: https://kccnceu2024.sched.com/event/1YeNk/the-data-pipelines-behind-forest-carbon-credits-why-pachama-uses-flyte-to-orchestrate-workflows-bernhard-stadlbauer-pachama
- Busca YouTube: https://www.youtube.com/results?search_query=The+Data+Pipelines+Behind+Forest+Carbon+Credits+%E2%80%93+Why+Pachama+Uses+Flyte+to+Orchestrate+Workflows+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Data Pipelines Behind Forest Carbon Credits – Why Pachama Uses Flyte to Orchestrate Workflows.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNk/the-data-pipelines-behind-forest-carbon-credits-why-pachama-uses-flyte-to-orchestrate-workflows-bernhard-stadlbauer-pachama
- YouTube search: https://www.youtube.com/results?search_query=The+Data+Pipelines+Behind+Forest+Carbon+Credits+%E2%80%93+Why+Pachama+Uses+Flyte+to+Orchestrate+Workflows+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nemlMo58BsI
- YouTube title: The Data Pipelines Behind Forest Carbon Credits – Why Pachama Uses Flyte to Orchestrate Workflows
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-data-pipelines-behind-forest-carbon-credits-why-pachama-uses-flyte/nemlMo58BsI.txt
- Transcript chars: 28396
- Keywords: flight, carbon, usually, workflow, machine, already, projects, pajama, generally, dependencies, around, features, important, course, possible, credits, question, whether

### Resumo baseado na transcript

good evening everyone uh thank you for making it to this very last session of today uh you probably all had a very long and exciting day I I did as well so glad that you all you all made it in this last session of the day I will be talking about the data pipelines behind carbon credits and why we as pajama chose flight as a workl orchestration system to power these these carbon credits uh maybe through a show of hand who here uses a workflow orchestrator

### Excerpt da transcript

good evening everyone uh thank you for making it to this very last session of today uh you probably all had a very long and exciting day I I did as well so glad that you all you all made it in this last session of the day I will be talking about the data pipelines behind carbon credits and why we as pajama chose flight as a workl orchestration system to power these these carbon credits uh maybe through a show of hand who here uses a workflow orchestrator so that I have a bit of an idea okay okay there's some um my name is Bernard in my day job am I I'm a Staff engineer at at pajama and in my free time I'm developing uh I'm contributing to the open source project flight I sit on the technical steering committee there I'm generally fairly involved uh if you want to get in I'm available after this talk I will be be around here there will be a question and answer session uh but feel free to also go to my website where you find links to most of my socials my GitHub my LinkedIn um and all of that today I will be talking about uh short intro to pajama what we generally do and intro to flight what it is and and roughly how it how it works why we as pajama chose to to use flight in airflow or Argo or cube flow or any of the other orchestrators out there um and this should be interesting because it might you might see features uh that you don't have in your workflo extion system and you can use this to evaluate uh when you want to choose a workfl station system and you don't have one yet uh you can use these questions to to evaluate uh whether that's useful to you and and in the end I'm going to talk about a few common pitfalls that I'm I'm seeing when people start out using flight uh there's one or two tricky bits that you uh you need to remember it first and just showing these because there are typical Things I See Art developers using so what is Pajama pajama tries to find the best carbon uh Forest Resto restoration and conservation projects and these projects typically sell carbon credits as a mean of their income they need to rent land they need to plant trees and usually carbon credits are a mean for them to restore land or to conserve land for the future one ton or one carbon credit is usually one ton of CO2 that's either uh restored or conserved so for you as a buyer it is important that the caring accounting is right so for you as a buyer it is important that when you offset a ton of carbon after you've reduced everything that you could sometimes you just n
