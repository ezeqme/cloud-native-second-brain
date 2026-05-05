---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Alexander Matyushentsev", "Akuity", "Leonardo Luz Almeida", "Intuit"]
sched_url: https://kccnceu2026.sched.com/event/2EIbg/the-10x-devops-engineers-toolkit-argo-cd-+-ai-driven-mcp-automation-alexander-matyushentsev-akuity-leonardo-luz-almeida-intuit
youtube_search_url: https://www.youtube.com/results?search_query=The+10x+DevOps+Engineer%E2%80%99s+Toolkit%3A+Argo+CD+%2B+AI-Driven+MCP+Automation+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The 10x DevOps Engineer’s Toolkit: Argo CD + AI-Driven MCP Automation - Alexander Matyushentsev, Akuity & Leonardo Luz Almeida, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alexander Matyushentsev, Akuity, Leonardo Luz Almeida, Intuit
- Schedule: https://kccnceu2026.sched.com/event/2EIbg/the-10x-devops-engineers-toolkit-argo-cd-+-ai-driven-mcp-automation-alexander-matyushentsev-akuity-leonardo-luz-almeida-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=The+10x+DevOps+Engineer%E2%80%99s+Toolkit%3A+Argo+CD+%2B+AI-Driven+MCP+Automation+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The 10x DevOps Engineer’s Toolkit: Argo CD + AI-Driven MCP Automation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EIbg/the-10x-devops-engineers-toolkit-argo-cd-+-ai-driven-mcp-automation-alexander-matyushentsev-akuity-leonardo-luz-almeida-intuit
- YouTube search: https://www.youtube.com/results?search_query=The+10x+DevOps+Engineer%E2%80%99s+Toolkit%3A+Argo+CD+%2B+AI-Driven+MCP+Automation+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iC15zeOLZQA
- YouTube title: The 10x DevOps Engineer’s Toolkit: Argo CD + AI-Dr... Alexander Matyushentsev & Leonardo Luz Almeida
- Match score: 0.759
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-10x-devops-engineers-toolkit-argo-cd-ai-driven-mcp-automation/iC15zeOLZQA.txt
- Transcript chars: 23492
- Keywords: argo, application, server, provide, client, understand, third-party, request, simple, support, specific, available, access, logs, extract, response, wanted, execute

### Resumo baseado na transcript

And today we're going to be presenting a new open source project that we've been working on, which is called MCP for Argo CD, as well as how how we're being using this project to solve real world problems. I've been working on rollouts, workflows, and Argo CD for almost a decade. The problem is there are so many third-party services that it's nearly impossible to build integration with all of them in a client. So in this example I'm demonstrating how client can execute sync action of Argo CD and payload is super simple. It has access to logs, live Kubernetes manifests, and I think it's fair to say it's more or less feature complete. One is kind of I would say very simple but it demonstrates what MCP can do.

### Excerpt da transcript

Hello everyone. Welcome to the Argo maintainers track at KubeCon. And today we're going to be presenting a new open source project that we've been working on, which is called MCP for Argo CD, as well as how how we're being using this project to solve real world problems. My name is Leonardo. I usually go by Leo. I'm a staff software developer at Intuit and also an Argo maintainer. Okay, hello everyone. Let me introduce myself. My name is Alexander Matushchenko. I work at company called Acuity. I'm a co-founder and chief architect. Also maintainer of Argo project. I've been working on rollouts, workflows, and Argo CD for almost a decade. And let's get started. I want to start from just giving you overview of what this talk is about. So I will cover half of this agenda. I will talk about why MCP is useful, why did we even choose to build MCP project for Argo CD, then I will cover the project itself, and share with you ideas we had and the use cases we were hoping to solve using MCP for Argo CD, and then I will get it will get it give it back to Leo where he can talk about how Intuit uses this project and how they what results they got and how they were able to help engineers to get more productive.

And with that, let's start from a little bit of theory. I want to explain why did we choose to even use MCP and what problem it's solving. So >> [clears throat] >> as you might know, large language models LLMs cannot really talk to third-party services. They cannot do anything in real world. They simply get request in form of text and they produce text in response and that's all they can do. So it's kind of boring and not so useful. But there is a simple way to make it more interactive. Request might specifically ask MCP to provide in response some metadata that explains an action that should be executed. And then AI client such as Cloud Code or Cursor or your favorite client supposed to parse the response and then do the action, call this third-party service that you want to integrate with and provide this response back to a model. And pretty much every company that >> [clears throat] >> does integration with LLMs already knows how to do it. And it's really not a difficult. There is a little bit of code that you need to write.

The problem is there are so many third-party services that it's nearly impossible to build integration with all of them in a client. And that's why MCP was born. MCP is just a protocol that is intended to be this universal connector betwe
