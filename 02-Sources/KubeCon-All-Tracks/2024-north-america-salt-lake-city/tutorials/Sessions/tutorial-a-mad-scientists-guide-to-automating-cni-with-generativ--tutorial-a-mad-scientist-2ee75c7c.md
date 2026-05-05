---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Tutorials"
themes: ["AI ML"]
speakers: ["Doug Smith", "Red Hat", "Inc"]
sched_url: https://kccncna2024.sched.com/event/1i7kI/tutorial-a-mad-scientists-guide-to-automating-cni-with-generative-ai-doug-smith-red-hat-inc
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+A+Mad+Scientist%27s+Guide+to+Automating+CNI+with+Generative+AI+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tutorial: A Mad Scientist's Guide to Automating CNI with Generative AI - Doug Smith, Red Hat, Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Doug Smith, Red Hat, Inc
- Schedule: https://kccncna2024.sched.com/event/1i7kI/tutorial-a-mad-scientists-guide-to-automating-cni-with-generative-ai-doug-smith-red-hat-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+A+Mad+Scientist%27s+Guide+to+Automating+CNI+with+Generative+AI+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tutorial: A Mad Scientist's Guide to Automating CNI with Generative AI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kI/tutorial-a-mad-scientists-guide-to-automating-cni-with-generative-ai-doug-smith-red-hat-inc
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+A+Mad+Scientist%27s+Guide+to+Automating+CNI+with+Generative+AI+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tEVoXKtymIA
- YouTube title: Tutorial: A Mad Scientist's Guide to Automating CNI with Generative AI - Doug Smith, Red Hat, Inc
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tutorial-a-mad-scientists-guide-to-automating-cni-with-generative-ai/tEVoXKtymIA.txt
- Transcript chars: 42024
- Keywords: running, actually, little, install, tutorial, plugins, interface, network, config, itself, create, generate, awesome, cuddle, whereabouts, llm, docker, information

### Resumo baseado na transcript

let's go ahead and get it kicked off thanks for taking the time to uh come to my tutorial session uh mad scientist guide to automating cni with generative AI uh my name is Doug Smith I work at red hat and I am heavily involved in the cni community so the container networking interface um and I had come up with a bit of a science experiment that I wanted to uh to share with you all that you're welcome to um participate in um and I am very

### Excerpt da transcript

let's go ahead and get it kicked off thanks for taking the time to uh come to my tutorial session uh mad scientist guide to automating cni with generative AI uh my name is Doug Smith I work at red hat and I am heavily involved in the cni community so the container networking interface um and I had come up with a bit of a science experiment that I wanted to uh to share with you all that you're welcome to um participate in um and I am very excited to to share this with you uh so without Much Ado let's get right into the agenda um which I'm going to start off by getting kind of a show of hands it'll help me sort of uh have a litness test for how deep I might go into this stuff so first question is uh who's coming to cubec con for the first time all right awesome good welcome to cubec con and psych that you came thanks for choosing my session for sure how about anyone who's used some kind of generative AI for text like chat gbt Gemini co-pilot all right good good awesome sweet tool use it wisely or use it in a crazy fashion like a mad scientist which is what we'll do today um so I'm going to guess that a lot of you know what an llm is show of hand cool yeah it's a large language model which is uh generative artificial intelligence for um generating text so okay kubernetes experience you don't really need to have much um who's used Cube cuddle before okay awesome lots of people excellent honestly uh you kind of don't even know how have to know how to use it um there should be a lot of uh copy and paste but if you can use Cube cuddle you're in really good shape for this uh for this tutorial uh who uses kind show of hands okay good number cool so we're going to use kind before it's kuber um we're going to use kind today uh that's kubernetes in Docker um which is kind of a handy dandy way to run run kubernetes and who knows what cni is okay good awesome all right so yeah good number of people so cni is uh the container networking interface it's an API that's sort of a like linga Fran for getting your networking components to speak to kubernetes it's actually its its own API so it is not the kubernetes API um which is a little bit um different has anyone actually written a cni configuration before show of hands okay just a couple cool well you're going to get a robot to do it um for you but if you've written one before um you're super ahead of the game uh awesome thank you so yeah today it's a tutorial so I'm G to try to keep my blabbing to a little bit of a minimu
