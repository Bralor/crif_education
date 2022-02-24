{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['append',\n",
      " 'clear',\n",
      " 'copy',\n",
      " 'count',\n",
      " 'extend',\n",
      " 'index',\n",
      " 'insert',\n",
      " 'pop',\n",
      " 'remove',\n",
      " 'reverse',\n",
      " 'sort']\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/python3.8\n",
    "from pprint import pprint\n",
    "\n",
    "no_magic_methods = [\n",
    "    method\n",
    "    for method in dir(list)\n",
    "    if not method.startswith(\"__\")\n",
    "]\n",
    "\n",
    "pprint(no_magic_methods)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
