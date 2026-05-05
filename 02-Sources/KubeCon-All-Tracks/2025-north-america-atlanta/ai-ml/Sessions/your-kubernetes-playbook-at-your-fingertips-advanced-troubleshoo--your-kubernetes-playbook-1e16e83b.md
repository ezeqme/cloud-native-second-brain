---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["David vonThenen", "NetApp", "Yash Sharma", "DigitalOcean"]
sched_url: https://kccncna2025.sched.com/event/27FZ8/your-kubernetes-playbook-at-your-fingertips-advanced-troubleshooting-with-mcp-rag-and-k8sgpt-david-vonthenen-netapp-yash-sharma-digitalocean
youtube_search_url: https://www.youtube.com/results?search_query=Your+Kubernetes+Playbook+at+Your+Fingertips%3A+Advanced+Troubleshooting+With+MCP%2C+RAG%2C+and+K8sgpt+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Your Kubernetes Playbook at Your Fingertips: Advanced Troubleshooting With MCP, RAG, and K8sgpt - David vonThenen, NetApp & Yash Sharma, DigitalOcean

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: David vonThenen, NetApp, Yash Sharma, DigitalOcean
- Schedule: https://kccncna2025.sched.com/event/27FZ8/your-kubernetes-playbook-at-your-fingertips-advanced-troubleshooting-with-mcp-rag-and-k8sgpt-david-vonthenen-netapp-yash-sharma-digitalocean
- Busca YouTube: https://www.youtube.com/results?search_query=Your+Kubernetes+Playbook+at+Your+Fingertips%3A+Advanced+Troubleshooting+With+MCP%2C+RAG%2C+and+K8sgpt+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Your Kubernetes Playbook at Your Fingertips: Advanced Troubleshooting With MCP, RAG, and K8sgpt.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZ8/your-kubernetes-playbook-at-your-fingertips-advanced-troubleshooting-with-mcp-rag-and-k8sgpt-david-vonthenen-netapp-yash-sharma-digitalocean
- YouTube search: https://www.youtube.com/results?search_query=Your+Kubernetes+Playbook+at+Your+Fingertips%3A+Advanced+Troubleshooting+With+MCP%2C+RAG%2C+and+K8sgpt+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SVLrY-KpTcE
- YouTube title: Your Kubernetes Playbook at Your Fingertips: Advanced Troubleshooti... David vonThenen & Yash Sharma
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/your-kubernetes-playbook-at-your-fingertips-advanced-troubleshooting-w/SVLrY-KpTcE.txt
- Transcript chars: 27725
- Keywords: cluster, runbook, embeddings, information, llm, security, question, language, playbook, server, actually, particular, practices, troubleshoot, models, organization, questions, endpoint

### Resumo baseado na transcript

I'll be honest like I am coming from the south of the India and for the past two days I was literally shaking too much and I was trying to figure out how I'm going to you know survive these two days. when we were talking I was talking with David now what should we put out and we figured out okay uh there is a much more better way coming up and there is a project called kids GPT uh to use MCP with Kubernetes to So, uh those who don't know this is a uh project which is helping you to troubleshoot your Kubernetes cluster, analyze your Kubernetes cluster with the help of AI. AI is coming up and we all know that it's been a decade that Kubernetes came up and now we we all are figuring out right uh to run AI workloads in the Kubernetes or sometime how to train AI workloads in the Kubernetes KGP focus on how you can uh make your process of troubleshooting Kubernetes easier with the help of AI get you better suggestion how you can improve or what's the error you're getting so it helps lets you uh troubleshoot your Kubernetes cluster with all lot So uh if we move forward uh I'll ask David to talk more about on how what we are going to talk or a demo on.

### Excerpt da transcript

Hello everyone. Uh can I have your attention please? I hope you had a great keynote today. Uh and uh you had some coffee. I'm I'm pretty happy with the weather today. I'll be honest like I am coming from the south of the India and for the past two days I was literally shaking too much and I was trying to figure out how I'm going to you know survive these two days. But hopefully I survived these two days with the coffee. But yeah uh yeah so we'll start with our talk today. Uh we will talking about your Kubernetes playbook at your fingertips. Quite an interesting topic. when we were talking I was talking with David now what should we put out and we figured out okay uh there is a much more better way coming up and there is a project called kids GPT uh to use MCP with Kubernetes to troubleshoot your Kubernetes and environment or the production so we were experimenting uh with the project and uh we have done some of our work and today in our talk we'll sharing about it so I think Yeah. So let's start with our introductions.

I'm Yash. I work at Digital Ocean as a developer advocate. I'm also a maintainer of a CNC project called Mishri. It's a cloud native manager. I have been contributing in CNC for the past three years and uh in a many way like through the events contributing to through the projects and many many things. I'm also open source contributor not only in the CNCF ecosystem but outside of the CNCF ecosystem as well. I love machines. Any kind of machines I love. And there's one fact I came up with is like the Firefox logo isn't a fox if you don't know. So it's actually uh it's not a fox. And I'll introduce to David. Hey David. Uh he's um he used to be my colleague, but yeah. Uh would you like >> So yeah, for sure. So hey, my name is David Vonenan. Um I work at NetApp. So I'm in the office of the CTO. I've been doing like AIM ML stuff for like a number of years. uh typically focused in NLP. So that's natural language processing. Um prior to that I was actually in the Kubernetes and CNCF ecosystems working on Kubernetes at VMware and also at EMC.

So that kind of dates me how far back it goes. Um but yeah no happy to be here with Yash here doing the talk and yeah let's jump into it. >> Okay thank you David. Uh let's jump with the next one. Okay so what is KJTP? How many of you are aware of this particular project right now in the CNCF ecosystem? Oh, quite quite a many people. So, uh those who don't know this is a uh project which is helping you to troub
