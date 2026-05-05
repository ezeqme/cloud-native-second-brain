---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQWc/the-state-of-k8sgpt-your-troubleshooting-companion-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=The+State+of+K8sGPT%3A+Your+Troubleshooting+Companion+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The State of K8sGPT: Your Troubleshooting Companion | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQWc/the-state-of-k8sgpt-your-troubleshooting-companion-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=The+State+of+K8sGPT%3A+Your+Troubleshooting+Companion+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The State of K8sGPT: Your Troubleshooting Companion | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQWc/the-state-of-k8sgpt-your-troubleshooting-companion-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=The+State+of+K8sGPT%3A+Your+Troubleshooting+Companion+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6KdBPjIZSok
- YouTube title: The State of K8sGPT: Your Troubleshooting Companion | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-state-of-k8sgpt-your-troubleshooting-companion-project-lightning-t/6KdBPjIZSok.txt
- Transcript chars: 5243
- Keywords: thought, integration, started, information, meanwhile, troubleshooting, everyone, issues, problems, automate, itself, easier, dealed, analyze, second, analyzers, analyzer, possible

### Resumo baseado na transcript

okay so hello everyone um yes today I will talk a bit about kid GPT in the state um kid GPT itself is a relatively new project so I think we started one year at this time ago whom of you ever heard about K GPT okay some of you perfect hopefully um I'll get some some new information for you um so first things first why did we start k um building cat GPT at first because AI was cool at this time so um we thought we have

### Excerpt da transcript

okay so hello everyone um yes today I will talk a bit about kid GPT in the state um kid GPT itself is a relatively new project so I think we started one year at this time ago whom of you ever heard about K GPT okay some of you perfect hopefully um I'll get some some new information for you um so first things first why did we start k um building cat GPT at first because AI was cool at this time so um we thought we have to do something with the AI um and thought this would be a good use case the first thing we found out is that troubleshooting kubernetes can be really hard so um the people who started with kgpt are old Su admins old sres and so on and um we all had some issues with konas we troubleshooted day by day and so on and we thought this this this should should get easier um and this brings me to the point we are troubleshooting the same issues over and over I think um many of us dealed with missing service accounts we all um dealed with labors um on on pots which are not there for services and so on and um we thought this could make it easier um we also thought that we as humans have the problems um but we also have the ability to find them and um the AI itself is able to provide solutions for our problems so for instance if we f um if we collect enough information to find out all of the related resources and so on um we could put this into an AI model and could say Yes um this is the problem so what is Kate's GPT at first um Kate's GPT initially was only a c um the First Command we had was kid GPT analyze and with K GPT analyze no wayi was in place um the second thing we had was some kind of explain mode which um sent some data to open ey and so on and got information for it so um the case GPT um CLI consists of some analyzers such as a port analyzer deployment analyzer and so on which tries to find problem patterns furthermore we have some kind of AI integration and in the meanwhile um we have many AI integration such as for openi vertex bedrock and also for um local gu and the interesting part is with the analyzers we try to um um find as many as much data as possible in our cluster and with the integration we try to interpret interpret it so in the end the cat GPT tells you that you have a problem and this is the solution without uh the integration it only tells you that you have a problem so a typical result of the kid GPT um CLI would look like this so um in fact This was um a problem that uh image could not be pulled so I tried to find the fi
