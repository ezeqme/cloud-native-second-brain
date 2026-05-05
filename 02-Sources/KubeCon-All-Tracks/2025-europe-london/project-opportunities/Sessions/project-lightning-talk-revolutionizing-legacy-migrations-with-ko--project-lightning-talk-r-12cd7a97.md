---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML"]
speakers: ["Jonah Sussman", "Developer / Approver"]
sched_url: https://kccnceu2025.sched.com/event/1tcwv/project-lightning-talk-revolutionizing-legacy-migrations-with-konveyor-ai-jonah-sussman-developer-approver
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Revolutionizing+Legacy+Migrations+with+Konveyor+AI+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Revolutionizing Legacy Migrations with Konveyor AI - Jonah Sussman, Developer / Approver

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]]
- País/cidade: United Kingdom / London
- Speakers: Jonah Sussman, Developer / Approver
- Schedule: https://kccnceu2025.sched.com/event/1tcwv/project-lightning-talk-revolutionizing-legacy-migrations-with-konveyor-ai-jonah-sussman-developer-approver
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Revolutionizing+Legacy+Migrations+with+Konveyor+AI+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Revolutionizing Legacy Migrations with Konveyor AI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcwv/project-lightning-talk-revolutionizing-legacy-migrations-with-konveyor-ai-jonah-sussman-developer-approver
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Revolutionizing+Legacy+Migrations+with+Konveyor+AI+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wO1bWs_LD8w
- YouTube title: Project Lightning Talk: Revolutionizing Legacy Migrations with Konveyor AI - Jonah Sussman
- Match score: 0.992
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-revolutionizing-legacy-migrations-with-konveyor/wO1bWs_LD8w.txt
- Transcript chars: 4331
- Keywords: conveyor, migrator, legacy, useful, migrations, analysis, applications, imagine, agentic, accept, reject, revolutionizing, locations, migrating, cloudnative, basically, source, issues

### Resumo baseado na transcript

I'm a software engineer at Red Hat and today I'm going to be talking about uh revolution revolutionizing legacy migrations with uh conveyor AI. So conveyor is a CNCF sandbox project that accelerates migration uh projects. So it's useful for those bespoke um complicated uh in-house solutions and also Kai learns over time. So if you want to get involved and learn more um you can find the project on GitHub. And then you can also reach us at the kuberneteslack.com on those channels conveyor and conveyor dev.

### Excerpt da transcript

All right. Hey everybody, my name is uh Jonah Susman. I'm a software engineer at Red Hat and today I'm going to be talking about uh revolution revolutionizing legacy migrations with uh conveyor AI. So first off, what is conveyor? So conveyor is a CNCF sandbox project that accelerates migration uh projects. So at its core, a migrator creates analysis rules to flag code locations to fix in many applications. Uh the surfaced info is especially useful for migrating tons of applications. So for example, let's say you're migrating from a really old framework and you want to make something cloudnative. It's really tough to do for one application. Imagine replicating it for 10 and then if you're on the order of 500 or more, it's it's intense. So uh the goal of course being more cloudnative technology usage. So on the left here you can see the conveyor operator UI. It has a a bunch of applications in various states of being migrated. And then on the right you can see an example of a rule. So the exact rule doesn't really matter but basically um this rule just says like legacy I should be avoided if anywhere in Java we find this just flag it for the migrator to go and take a look.

So on to conveyor AI or Kai um uh conveyor's data is a playground for AI if you can imagine. Um so Kai utilizes this body of data available in conveyor to generate recommendations for a migrator to use. So here's a little um diagram of how the structure of Kai. So we've got legacy source code and the data that's present in conveyor and then we've got analysis issues. So a migrator might take a couple issues and say hey I want to fix these. So uh we also have some solved examples of how those rules were solved in the past and I'll get to how those are generated in a second that gets funneled into a prompt which then goes into an agentic workflow. And if you're unfamiliar with agentic workflows basically it's an LLM that integrates external tools such as llinters compilers tests etc. and an LLM iteratively iterates with it to say hey this is what I want to do here's how I accomplish it um like if for example if we want to migrate Java uh we say hey I'm going to need access to a Java compiler we're going to have a Java llinter maybe access to the file system etc and it iteratively goes over and over until um a satisfactory result is produced so then we have that result and that's get p get that gets passed to the user via an IDE extension and the ID the user can either accept it or reject it
