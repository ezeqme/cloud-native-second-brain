---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Hillai Ben-Sasson", "Nir Ohfeld", "Wiz"]
sched_url: https://kccncna2025.sched.com/event/27FeS/the-good-the-bad-and-the-ugly-hacking-3-cloud-native-ai-services-with-1-vulnerability-hillai-ben-sasson-nir-ohfeld-wiz
youtube_search_url: https://www.youtube.com/results?search_query=The+Good%2C+the+Bad%2C+and+the+Ugly%3A+Hacking+3+Cloud+Native+AI+Services+With+1+Vulnerability+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Good, the Bad, and the Ugly: Hacking 3 Cloud Native AI Services With 1 Vulnerability - Hillai Ben-Sasson & Nir Ohfeld, Wiz

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Atlanta
- Speakers: Hillai Ben-Sasson, Nir Ohfeld, Wiz
- Schedule: https://kccncna2025.sched.com/event/27FeS/the-good-the-bad-and-the-ugly-hacking-3-cloud-native-ai-services-with-1-vulnerability-hillai-ben-sasson-nir-ohfeld-wiz
- Busca YouTube: https://www.youtube.com/results?search_query=The+Good%2C+the+Bad%2C+and+the+Ugly%3A+Hacking+3+Cloud+Native+AI+Services+With+1+Vulnerability+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Good, the Bad, and the Ugly: Hacking 3 Cloud Native AI Services With 1 Vulnerability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FeS/the-good-the-bad-and-the-ugly-hacking-3-cloud-native-ai-services-with-1-vulnerability-hillai-ben-sasson-nir-ohfeld-wiz
- YouTube search: https://www.youtube.com/results?search_query=The+Good%2C+the+Bad%2C+and+the+Ugly%3A+Hacking+3+Cloud+Native+AI+Services+With+1+Vulnerability+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZTiWXqYg97U
- YouTube title: The Good, the Bad, and the Ugly: Hacking 3 Cloud Native AI Service... Hillai Ben-Sasson & Nir Ohfeld
- Match score: 0.848
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-good-the-bad-and-the-ugly-hacking-3-cloud-native-ai-services-with/ZTiWXqYg97U.txt
- Transcript chars: 31968
- Keywords: container, basically, access, actually, vulnerability, server, nvidia, replicate, environment, security, research, vulnerabilities, interesting, cluster, database, command, exploit, running

### Resumo baseado na transcript

Last year, our team at WH found a critical container escape vulnerability in a little known but very popular software component found in basically every AI cloud provider. And with just one vulnerability affecting basically the entire cloud ecosystem, we set out to find to find out how does each vendor handles a brand new zero day vulnerability. And because we're security researchers, what we actually asked ourself is what's the potential attack surface. But once again, we didn't find anything interesting, but it's a Kubernetes node. It has Kubernetes credentials like take these credentials and access the Kubernetes API server. But once again, we were out of luck and we had no access to to the Kubernetes API server due to network restrictions.

### Excerpt da transcript

and welcome to our talk the good, the bad, and the ugly. Hacking three cloudnative AI services with just one vulnerability. Last year, our team at WH found a critical container escape vulnerability in a little known but very popular software component found in basically every AI cloud provider. And with just one vulnerability affecting basically the entire cloud ecosystem, we set out to find to find out how does each vendor handles a brand new zero day vulnerability. So let's dive in. So just a quick who are we before we begin. My name is Narfield and I'm the head of vulnerability research at Whiz and here with me on stage is Eli Ben Sason, one of our senior security researchers. We are both security researchers based in Israel and we specialize in cloud security research. But actually in the last two years we actually shifted our focus from cloud security research to AI cloud security research. And what does that even mean? It means looking and finding vulnerabilities in the entire AI pipeline from AI data sharing vulnerabilities where we uncovered 38 terabytes of internal Microsoft training data or finding an exposed deepseek database exposing user prompts and predictions to finding service stakehold vulnerabilities in the AI in the biggest AI as a service providers such [clears throat] as highace replicate and SAS SAP and and after finding all of these vulnerabilities, we decided to shift our focus to look at the AI infrastructure itself which be the focus of today's talk.

We found vulnerabilities in radius invon and inv container toolkit. So before we can start talking about AI infrastructure vulnerabilities, we need to understand what's AI infrastructure. basically answering the question of how do I run AI? Okay, we're a company and you want to start training your own AI model and serve it. So the first thing you know you are going to need to do is gather all of your data and put it in some some sort of a database. Then once you have the data you you'll use some kind of a training framework to turn this data into a model. And once you have a your model ready, you can use some kind of of an inference server to serve and infer your model. Okay. So after researching and finding critical vulnerabilities in most of these products, we thought what if there's a level deeper something beneath all of this that is in common with everything [clears throat] related to AI. And the answer was quite simple. Nvidia GPUs. Nvidia GPUs are basically everywhere when it
