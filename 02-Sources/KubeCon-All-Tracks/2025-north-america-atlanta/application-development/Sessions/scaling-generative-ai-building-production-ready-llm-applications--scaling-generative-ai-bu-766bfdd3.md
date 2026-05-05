---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Application Development"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Daniel Oh", "Kevin Dubois", "IBM"]
sched_url: https://kccncna2025.sched.com/event/27FWH/scaling-generative-ai-building-production-ready-llm-applications-daniel-oh-kevin-dubois-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+Generative+AI%3A+Building+Production-Ready+LLM+Applications+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Scaling Generative AI: Building Production-Ready LLM Applications - Daniel Oh & Kevin Dubois, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Daniel Oh, Kevin Dubois, IBM
- Schedule: https://kccncna2025.sched.com/event/27FWH/scaling-generative-ai-building-production-ready-llm-applications-daniel-oh-kevin-dubois-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+Generative+AI%3A+Building+Production-Ready+LLM+Applications+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Scaling Generative AI: Building Production-Ready LLM Applications.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWH/scaling-generative-ai-building-production-ready-llm-applications-daniel-oh-kevin-dubois-ibm
- YouTube search: https://www.youtube.com/results?search_query=Scaling+Generative+AI%3A+Building+Production-Ready+LLM+Applications+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XtNc4xXIe6Y
- YouTube title: Scaling Generative AI: Building Production-Ready LLM Applications - Daniel Oh, Red Hat
- Match score: 0.957
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/scaling-generative-ai-building-production-ready-llm-applications/XtNc4xXIe6Y.txt
- Transcript chars: 25228
- Keywords: application, actually, developer, probably, engineering, question, capability, daniel, create, automatically, pretty, external, source, whatever, container, platform, simple, sending

### Resumo baseado na transcript

So I'm going to talk a little bit about today like a geni and a little bit agent AI and then how to make a great AI application in production and then I got a two quick question before I'm getting started. And how many people are actually like some responsible for AI engineer? AI actually came out almost 100 years ago like many decades ago and at a time we named on artificial intelligence and then it keep evolving into like a machine learning deep learning and genai two and a half years ago from open AI and So that's why how do you ask a question more like a smarter better that is a pro engineering and then you also have a many different AI model and you got to answer so that is how it works so the problem is that hard to find the right model for you just imagine that 10 years ago Kubernetes came out and container technology came out and Now after a couple months later or six months later you when you go to container registry for example docker registry you can find the millions of container images which container image you will be better for you on your java or net application you cannot find out in five minute so you're going to give it a try and error and so on as your architecture

### Excerpt da transcript

So I'm going to talk a little bit about today like a geni and a little bit agent AI and then how to make a great AI application in production and then I got a two quick question before I'm getting started. How many people uh are Java developer here? Any Java experience? Awesome. A lot of that. And how many people are actually like some responsible for AI engineer? Wow, a lot. That's cool. So my name is Daniel. I'm from Boston, United States. I'm a longtime CNCF ambassador and then like a track chair and among others and a lot of community contribution. If you joined the keynote yesterday, you probably saw me and during the keynote share the CNCF stuff and I'm also Java champion for a long time and uh here's my contact Daniel O3. So when I create the Daniel O like handler, social media, GitHub among others, there are many Daniel around the world. So I try to uh find the Daniel Oro uh one two three four five six something like that and I end up with Daniel number 30. So that's why I have Daniel 30. So you can find me any social media like X.com and LinkedIn and blue sky and GitHub and YouTube channel as well.

So please find me and reach out to me if there any question about this topic and Java and cloud and CNCF. I'm happy to chat with us. Okay. So let me uh little bit one step back try to understand the journey of Genai and NMS. So people maybe I know you guys already have great experience AI stuff for the last two days and then in many other conferences and the YouTube channel and the blog post and so on but sometimes some people actually misunderstand uh when the AI actually came out. AI actually came out almost 100 years ago like many decades ago and at a time we named on artificial intelligence and then it keep evolving into like a machine learning deep learning and genai two and a half years ago from open AI and a lot of companies jump into that market and the Google Gemini and open air ch and then deepse R1 and the Grog and many others you're probably using AI tool every single day I actually using more than 10 AI tools and you know what so my uh first death slide I actually generate this imagy the hydrobot the city view from Google Gemini I actually don't know this accurate or not please tell me if you're living in this city a lovely city my first visiting but I've been uh India a lot of time but this city first time just tell me this isn't correct or not after that Okay.

So, and then now people more are talking about agentic AI. So, agentic AI is
