---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["Cloud Native"]
speakers: ["Phillip Carter", "Honeycomb"]
sched_url: https://kccncna2023.sched.com/event/1R2pL/observing-a-large-language-model-in-production-phillip-carter-honeycomb
youtube_search_url: https://www.youtube.com/results?search_query=Observing+a+Large+Language+Model+in+Production+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Observing a Large Language Model in Production - Phillip Carter, Honeycomb

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[Cloud Native]]
- País/cidade: United States / Chicago
- Speakers: Phillip Carter, Honeycomb
- Schedule: https://kccncna2023.sched.com/event/1R2pL/observing-a-large-language-model-in-production-phillip-carter-honeycomb
- Busca YouTube: https://www.youtube.com/results?search_query=Observing+a+Large+Language+Model+in+Production+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Observing a Large Language Model in Production.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2pL/observing-a-large-language-model-in-production-phillip-carter-honeycomb
- YouTube search: https://www.youtube.com/results?search_query=Observing+a+Large+Language+Model+in+Production+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KRsxuY1sZ_E
- YouTube title: Observing a Large Language Model in Production - Phillip Carter, Honeycomb
- Match score: 0.866
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/observing-a-large-language-model-in-production/KRsxuY1sZ_E.txt
- Transcript chars: 32914
- Keywords: actually, language, observability, pretty, little, models, prompt, probably, feature, object, product, honeycomb, somebody, particular, production, against, response, single

### Resumo baseado na transcript

okay um it's been about another minute so I think I'll go ahead and get going um first of all thank you all for coming I know it's like 5:30 pretty close to dinner time uh if youall are hungry I um I won't feel offended if you got to duck out because you just got to eat some food um I'm feeling pretty hungry myself soon so looking forward to eating after this um I won't try to keep you forever uh so this is going to be a

### Excerpt da transcript

okay um it's been about another minute so I think I'll go ahead and get going um first of all thank you all for coming I know it's like 5:30 pretty close to dinner time uh if youall are hungry I um I won't feel offended if you got to duck out because you just got to eat some food um I'm feeling pretty hungry myself soon so looking forward to eating after this um I won't try to keep you forever uh so this is going to be a fun topic I think at least fun for me um because this is squarely at the intersection of two talk tracks I guess uh there's the ML and AI track and there's the observability track and the two are very firmly intertwined in in this talk so if you're familiar with one but not the other then hopefully you'll find some stuff that's useful here if you're not familiar with either uh you might be able to bookmark some of the stuff after you go learn a little bit more about um some of the others but regardless um let's get going so I want to talk about I call it observing an LM in production but this is really about ways that you can make large language models more reliable in production and um the impetus behind this is is you are likely aware pretty much every organization in the planet right now is looking to build with large linguage modules to some extent and they're really really powerful but they're kind of hard uh it's not magic there's a lot of problems that they bring and a lot of challenges is that a lot of teams may not have necessarily been prepared to handle uh we were one of those and so I want to walk through some of our case study at honeycomb where we learned a whole lot um but I want to spend a little bit of time on why large language models are hard in production so I would posit that your average engineer who knows a thing or two about the product that you're working on if given an afternoon could probably cough up some sort of prot protype that does something pretty useful with an llm that's that's some of the incredible power and I think it I just want to underscore how amazing it is that we have literally the world's most powerful machine learning models just available from a single API call like I could never have dreamed that we had this kind of power uh available to us but with that comes a whole set of problems that we may not have knew that we would have um and to extend that I would say it's actually fairly easy to take a feature that uses a large language model to market for you know something that's experimental or
