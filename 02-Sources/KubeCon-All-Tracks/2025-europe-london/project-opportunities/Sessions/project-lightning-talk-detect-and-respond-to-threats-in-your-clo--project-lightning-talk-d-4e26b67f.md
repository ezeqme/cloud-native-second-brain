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
themes: ["AI ML", "Community Governance"]
speakers: ["Luca Guerra", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcw6/project-lightning-talk-detect-and-respond-to-threats-in-your-cloud-infrastructure-with-falco-luca-guerra-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Detect+and+Respond+to+Threats+in+Your+Cloud+Infrastructure+With+Falco+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Detect and Respond to Threats in Your Cloud Infrastructure With Falco - Luca Guerra, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Luca Guerra, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcw6/project-lightning-talk-detect-and-respond-to-threats-in-your-cloud-infrastructure-with-falco-luca-guerra-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Detect+and+Respond+to+Threats+in+Your+Cloud+Infrastructure+With+Falco+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Detect and Respond to Threats in Your Cloud Infrastructure With Falco.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcw6/project-lightning-talk-detect-and-respond-to-threats-in-your-cloud-infrastructure-with-falco-luca-guerra-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Detect+and+Respond+to+Threats+in+Your+Cloud+Infrastructure+With+Falco+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RGLy_JtGD9U
- YouTube title: Project Lightning Talk: Detect and Respond to Threats in Your Cloud Infrastructure Wi... Luca Guerra
- Match score: 0.995
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-detect-and-respond-to-threats-in-your-cloud-inf/RGLy_JtGD9U.txt
- Transcript chars: 4429
- Keywords: journey, events, environment, kernel, maintainer, infrastructure, everything, simple, outputs, little, maintainers, security, install, clusters, write, perfectly, engineer, alerts

### Resumo baseado na transcript

I'm one of the maintainers and if you didn't know about Falco, Falco is graduated project from CNCF that monitors your infrastructure for security events. So you install it on your clusters, on your Kubernetes clusters, on your nodes, on your containerized environment and Falco looks at everything that happens in this node and will alert you on everything that you think is a security relevant event. So, Falco does not just take events from the kernel and reads them and outputs through and outputs alerts. You can take them from Kubernetes cluster, from your cloud account events and from a lot of other things. It's a mean that something is not going is going to be there and you were not expecting it to be maybe a chrome job that does some file access whatever and then if you like it you will learn how it works and you will learn how rules work and you will learn how to customize them so that they fit your environment a little bit better and then you can be perfectly happy with it but many people after a while they will start using our integrations I

### Excerpt da transcript

Hey everyone, I'm Luca and let's talk about Falco. I'm one of the maintainers and if you didn't know about Falco, Falco is graduated project from CNCF that monitors your infrastructure for security events. So you install it on your clusters, on your Kubernetes clusters, on your nodes, on your containerized environment and Falco looks at everything that happens in this node and will alert you on everything that you think is a security relevant event. How does it do it? It uses very simple rules that are designed to be simple to read and to write. So those rules are based on system calls in the Linux kernel. But even if you're not an expert in system calls, you work very far from the kernel. You don't need to be one. You you just you can simply read this rule and perfectly understand what it does. Uh even if you do front end all day, I went to front end engineer and and asked and I completely understood fore rules. So, as easy it is to write and read rules, it's easy to get the alerts. It's simple text.

It's a text message that you can see that not only has a specific event, but also the context about your Kubernetes cluster, your cloud infrastructure and everything that is around the specific event. So, uh, Falco over the year became far more than that. So, Falco does not just take events from the kernel and reads them and outputs through and outputs alerts. Today, you can ingest events from a lot of different areas, from a lot of different sources. You can take them from Kubernetes cluster, from your cloud account events and from a lot of other things. And you can output them to your CM to cues to a lot of other places. It would take me far more than five minutes to to tell tell you about all of these things. And when I was talking about these kind of things last week with the CNCF community group, they asked, "So, it's great. It's got a response engine and all, but I never use Falco. What what would my journey be like if today I started using Falco from scratch?" And uh I'm here to answer that question because I think it was a cool question.

So at first if you try you will discover what's happening and I can tell you this is not just going to be a journey of discovery about what Falco does and doesn't do and if it's good for you but it will be a journey about discovering yourself as well because I am sure that when you install Falco you will find out that your nodes are doing something that you're not expecting. I'm not saying that you're under attack.
