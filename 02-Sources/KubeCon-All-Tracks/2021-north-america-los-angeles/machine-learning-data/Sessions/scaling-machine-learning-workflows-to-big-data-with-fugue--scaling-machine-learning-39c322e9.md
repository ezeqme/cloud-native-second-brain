---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "SRE Reliability"]
speakers: ["Kevin Kho", "Prefect", "Han Wang", "Lyft"]
sched_url: https://kccncna2021.sched.com/event/lV5X/scaling-machine-learning-workflows-to-big-data-with-fugue-kevin-kho-prefect-han-wang-lyft
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+Machine+Learning+Workflows+to+Big+Data+with+Fugue+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Scaling Machine Learning Workflows to Big Data with Fugue - Kevin Kho, Prefect & Han Wang, Lyft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Kevin Kho, Prefect, Han Wang, Lyft
- Schedule: https://kccncna2021.sched.com/event/lV5X/scaling-machine-learning-workflows-to-big-data-with-fugue-kevin-kho-prefect-han-wang-lyft
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+Machine+Learning+Workflows+to+Big+Data+with+Fugue+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Scaling Machine Learning Workflows to Big Data with Fugue.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV5X/scaling-machine-learning-workflows-to-big-data-with-fugue-kevin-kho-prefect-han-wang-lyft
- YouTube search: https://www.youtube.com/results?search_query=Scaling+Machine+Learning+Workflows+to+Big+Data+with+Fugue+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fDIRMiwc0aA
- YouTube title: Scaling Machine Learning Workflows to Big Data with Fugue - Kevin Kho, Prefect & Han Wang, Lyft
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/scaling-machine-learning-workflows-to-big-data-with-fugue/fDIRMiwc0aA.txt
- Transcript chars: 23145
- Keywords: pandas, function, python, transform, category, execution, predict, schema, training, machine, column, engine, change, sample, simple, native, distributed, learning

### Resumo baseado na transcript

hi everyone thank you um it's i know we're at an infrastructure conference so it's nice to see fellow machine learning practitioners or people interested in machine learning um so yeah welcome to scaling machine learn machine workflow machine learning workflows with big data to big data with view so we're going to start off with a demo presented by han in this demo we're going to start out with a small panda size data frame and then we're going to apply some business logic to that and trans and

### Excerpt da transcript

hi everyone thank you um it's i know we're at an infrastructure conference so it's nice to see fellow machine learning practitioners or people interested in machine learning um so yeah welcome to scaling machine learn machine workflow machine learning workflows with big data to big data with view so we're going to start off with a demo presented by han in this demo we're going to start out with a small panda size data frame and then we're going to apply some business logic to that and trans and and bring that into spark and in the process we're going to see how much of code is needed to bring it to spark how much pandas and spark are different from each other and how the fugue opens how the open source library field can help you do this change okay hello everyone my name is han wong and today i'm going to do a quick demo of some very interesting features of fugue and i'm going to switch between python code spark code and figure code it's okay if you are not familiar with with spark and if you cannot follow on the spark part because uh that is just used to compare with fugue um and i think the most important thing is just to focus on how you solve this problem how intuitive your own expression should be when you want to solve this problem okay now let's start the first example is um we have a very interesting business logic which i guess if you're working a company you will always have some tricky logic where in this logic we have we are going to process the data frame and here is the business logic we have four columns a b c d they are all strings and for any given row if the number of non-null values is less than two then we drop the row and then otherwise we concatenate the non-null columns in order and output the value as e-column and also keep the original columns right this is not so difficult and the most intuitive way to express this logic i think is in this way you should take an iterable of lift as a list of values and then yield those values when it meets the criteria right this is just python code and also this code is very testable so now let's just write as you can see the last two rows will be dropped because there are too many nuns okay so this is the logic and now let's build some um sample data for us to work on and you don't have to care about this function just look at this data frame so this data frame has four columns a b c d and it has some nouns right so now the question is very simple how can you apply this function onto this sample
